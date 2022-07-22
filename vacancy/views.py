from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import (
    ListView, 
    DeleteView,
    DetailView,
)
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils import timezone as tz
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from main.decorators import hirer_required, employee_required
from main.utils import get_footer
from employee.models import Employee, CV, ChosenVacancy
from .models import Vacancy, NeededLanguage,VacancySerializer
from articles.views import favourite_articles
from contacts.models import Contact
from .forms import VacancyCreateForm
import pprint


@hirer_required
@login_required
def vacancy_create(request):
    if request.POST:
        data = dict(request.POST)
        new_vacancy_form = VacancyCreateForm(request.POST)
        new_vacancy = new_vacancy_form.save(commit=False)
        new_vacancy.creator = request.user
        new_vacancy.save()
        new_vacancy.cv_set.add(*list(CV.objects.filter(position=new_vacancy.position)))
        new_vacancy.save()
        new_contact = Contact.objects.create(
            content=f'{data["name"][0]}\n{data["phone_number"][0]}\n{data["email"][0]}',
            vacancy=new_vacancy)
        for i in range(len(data['language'])):
            new_lang = NeededLanguage.objects.create(
                vacancy=new_vacancy,
                language=data['language'][i],
                level=data['level'][i]
            )
        return redirect(reverse('my-vacancies'))
    return render(request, 'vacancy/vacancy_create.html')


@hirer_required
@login_required
def edit_vacancy(request, id):
    vacancy = Vacancy.objects.get(id=id)
    if request.POST:
        data = dict(request.POST)
        new_vacancy_form = VacancyCreateForm(request.POST, instance=vacancy)
        if new_vacancy_form.is_valid():
            new_vacancy_form.save()
            vacancy.cv_set.clear()
            vacancy.cv_set.add(*list(CV.objects.filter(position=vacancy.position)))
            vacancy.creation_date = tz.now()
            vacancy.save()
            vacancy.neededlanguage_set.all().delete()
            for i in range(len(data['language'])):
                new_lang = NeededLanguage.objects.create(
                    vacancy=vacancy,
                    language=data['language'][i],
                    level=data['level'][i]
                )
            return redirect('my-vacancy-info', id)
    context = {
        'vacancy': vacancy
    }
    return render(request, 'vacancy/edit.html', context)


class VacancyListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Vacancy
    ordering = ['-date_posted']

    def test_func(self):
        return hasattr(self.request.user, 'employee')


class VacancyDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Vacancy

    def test_func(self):
        vacancy = self.get_object()
        return hasattr(self.request.user, 'employee') or vacancy.creator == self.request.user


@hirer_required
@login_required
def delete_my_vacancy(request, pk):
    vacancy = Vacancy.objects.get(id=pk)
    if vacancy.creator == request.user:
        vacancy.delete()
    return redirect(reverse('my-vacancies'))


@login_required
def vacancy_edit(request, pk):
    vacancy = Vacancy.objects.get(pk=pk)

    if request.user != vacancy.creator:
        messages.add_message(
            request, 
            messages.ERROR, 
            'You can only edit your own vacancies!'
        )
        return redirect('home')
    
    if request.method == 'POST':
        pass


@hirer_required
@login_required
def refresh(request, id):
    vacancy = Vacancy.objects.get(id=id)
    if vacancy.creator == request.user:
        vacancy.creation_date = tz.now()
        vacancy.save()
    return redirect(request.META.get('HTTP_REFERER'))


@hirer_required
@login_required
def my_vacancies(request):
    context = {
        'vacancies': Vacancy.objects.filter(creator=request.user)
    }
    return render(request, 'vacancy/my_vac.html', context)


class MyVacancyDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Vacancy
    template_name = 'vacancy/my_vacancy_detail.html'

    def test_func(self):
        if not hasattr(self.request.user, 'hirer'):
            return False
        vacancy = self.get_object()
        return vacancy.creator == self.request.user


class VacancyDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Vacancy
    template_name = 'vacancy/vacancy_detail.html'

    def get(self, request, *args, **kwargs):
        vacancy = self.get_object()
        vacancy.views += 1
        vacancy.save()
        return super().get(request, *args, **kwargs)

    def test_func(self):
        return hasattr(self.request.user, 'employee')


def get_vacancies(request, n):
    vacancies = Vacancy.objects.all()[n:n+20]
    serializer = VacancySerializer(vacancies, many=True)
    data = [dict(i) for i in list(serializer.data)]
    return JsonResponse(data, safe=False, status=201)


@api_view(('GET',))
@employee_required
@login_required
def add_to_chosen(request, id):
    vacancy = Vacancy.objects.get(id=id)
    try:
        chosen = ChosenVacancy.objects.get(
            employee=request.user.employee,
            vacancy=vacancy
            )
    except Exception:
        chosen = None
    if not chosen:
        chosen = ChosenVacancy.objects.create(
            employee=request.user.employee,
            vacancy=vacancy
        )
    else:
        chosen.delete()
    return Response(status=status.HTTP_202_ACCEPTED)


@employee_required
@login_required
def chosen_vacancies(request):
    vacancies = [chosen.vacancy for chosen in request.user.employee.chosenvacancy_set.all()]
    articles = favourite_articles(request)
    context = {
        'vacancies': vacancies,
        'articles': articles,
    }
    return render(request, 'vacancy/chosen.html', context)


@employee_required
@login_required
def suitable_vacancies(request, id):
    cv = CV.objects.get(id=id)
    context = {
        'vacancies': cv.suitable_vacancies.all()
    }
    return render(request, 'vacancy/suitable_vacancies.html', context)


@hirer_required
@login_required
def response_notifications(request):
    vacancies = Vacancy.objects.filter(creator=request.user)
    context = {
        'vacancies': vacancies
    }
    context.update(get_footer())
    return render(request, 'vacancy/response_notifications.html', context)


@hirer_required
@login_required
def vacancy_responses(request, pk):
    vacancy = get_object_or_404(Vacancy, id=pk)
    context = {
        'vacancy': vacancy,
        'responses': vacancy.response_set.all(),
    }
    context.update(get_footer())
    return render(request, 'vacancy/vacancy_responses.html', context)