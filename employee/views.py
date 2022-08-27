import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    ListView,
    DetailView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.utils import timezone as tz
from rest_framework import status
from rest_framework.response import Response as r
from rest_framework.decorators import api_view
from main.decorators import login_forbidden, employee_required, hirer_required
from main.utils import send_activation_email
from vacancy.models import Vacancy
from contacts.models import ChosenContact
from articles.views import favourite_articles
from .models import (
    CV, ChosenCv, 
    KnownLanguage, KnownProgram, 
    Education, WorkExperience,
    CVSerializer
)
from .forms import *
from pprint import pprint


@login_forbidden
def employee_create(request, *args):
    if request.method == 'POST':
        u_form = UserCreateForm(request.POST)
        e_form = EmployeeCreateForm(
            request.POST
        )
        print(request.POST.get('email'))
        print(u_form.errors.items())
        print(e_form.errors.items())
        try:
            birth_date = datetime.date(
                int(request.POST.get('birth_date__year')), 
                int(request.POST.get('birth_date__month')),
                int(request.POST.get('birth_date__date'))
            )
        except Exception:
            birth_date = Nonde
        if u_form.is_valid() and e_form.is_valid() and birth_date:
            print('Both valid')
            try:
                if User.objects.get(email=request.POST.get('email')):
                    messages.add_message(
                        request, 
                        messages.ERROR, 'User with this email already exists'
                    )
                    u_form = UserCreateForm()
                    e_form = EmployeeCreateForm()
                    context = {
                        'u_form': u_form,
                        'e_form': e_form,
                    }
                    return render(request, 'employee/employee_create.html', context)

            except Exception as identifier:
                print(identifier)
            
            user = u_form.save(commit=False)
            user.username = user.email
            user.is_active = False
            user.save()
            employee = e_form.save(commit=False)
            employee.user = user
            employee.birth_date = birth_date
            employee.save()
            sent = send_activation_email(user, request)
            if not sent:
                messages.add_message(
                    request, 
                    messages.ERROR, 
                    'Something went wrong, please try again.'
                )
                user.delete()
            else:
                messages.add_message(
                    request, 
                    messages.SUCCESS, 
                    'Email has been sent to your account!'
                )
                return redirect(reverse('activate-message'))
        else:
            messages.add_message(
                request, 
                messages.ERROR, 'Please type in correct data'
            )
    return render(request, 'employee/employee_create.html')


@employee_required
@login_required
def create_cv(request, *args):
    if request.method == 'POST':
        data = dict(request.POST)
        cv_form = CVCreationForm(request.POST)
        if not cv_form.is_valid():
            print('Not valid')
            print(cv_form.errors)
            return redirect(reverse('create-cv'))
        new_cv = cv_form.save(commit=False)
        new_cv.birth_date = datetime.date(
                int(data['birth_date__year'][0]), 
                int(data['birth_date__month'][0]),
                int(data['birth_date__date'][0])
            )
        new_cv.about = data['about'][0]
        new_cv.employee = request.user.employee
        new_cv.save()
        new_cv.suitable_vacancies.add(*list(Vacancy.objects.filter(position=new_cv.position)))
        new_cv.save()
        for i in range(len(data['language'])):
            new_lang = KnownLanguage.objects.create(
                cv=new_cv,
                language=data['language'][i],
                level=data['lang__lev'][i]
            )
        for i in range(len(data['program'])):
            new_prog = KnownProgram.objects.create(
                cv=new_cv,
                program=data['program'][i]
            )
        exp_positions = data.get('exp_position')
        if exp_positions:
            for i in range(len(exp_positions)):
                new_exp = WorkExperience.objects.create(
                    cv=new_cv,
                    position=data['exp_position'][i],
                    org_name=data['org_name'][i],
                    responsibilities=data['responsibilities'][i],
                    start_year=datetime.date(
                        int(data['exp_start__year'][i]), 
                        int(data['exp_start__month'][i]),
                        1
                    ),
                    end_year=datetime.date(
                        int(data['exp_end__year'][i]), 
                        int(data['exp_end__month'][i]),
                        1
                    )
                )
        edu_degrees = [key for key in data.keys() if key.startswith('edu_degrees')]
        for i in range(len(data['establishment'])):
            new_education = Education.objects.create(
                cv=new_cv,
                degree=data[edu_degrees[i]][0],
                establishment=data['establishment'][i],
                faculty=data['faculty'][i],
                specialization=data['specialization'][i],
                start_year=data['start_year_edu'][i],
                end_year=data['end_year_edu'][i]
            )
        return redirect(reverse('my-cv'))
    return render(request, 'employee/cv_create.html')

@employee_required
@login_required
def edit_cv(request, id):
    cv = CV.objects.get(id=id)
    if request.method == 'POST':
        data = dict(request.POST)
        cv_form = CVCreationForm(request.POST, instance=cv)
        if not cv_form.is_valid():
            print('Not valid')
            print(cv_form.errors)
            return redirect(reverse('create-cv'))
        cv_form.save(commit=False)
        cv.birth_date = datetime.date(
                int(data['birth_date__year'][0]), 
                int(data['birth_date__month'][0]),
                int(data['birth_date__date'][0])
            )
        cv.about = data['about'][0]
        cv.save()
        cv.suitable_vacancies.clear()
        cv.suitable_vacancies.add(*list(Vacancy.objects.filter(position=cv.position)))
        cv.save()
        cv.cvattr_set.all().delete()
        for i in range(len(data['language'])):
            new_lang = KnownLanguage.objects.create(
                cv=cv,
                language=data['language'][i],
                level=data['lang__lev'][i]
            )
        for i in range(len(data['program'])):
            new_prog = KnownProgram.objects.create(
                cv=cv,
                program=data['program'][i]
            )
        for i in range(len(data['exp_position'])):
            new_exp = WorkExperience.objects.create(
                cv=cv,
                position=data['exp_position'][i],
                org_name=data['org_name'][i],
                responsibilities=data['responsibilities'][i],
                start_year=datetime.date(
                    int(data['exp_start__year'][i]), 
                    int(data['exp_start__month'][i]),
                    1
                ),
                end_year=datetime.date(
                    int(data['exp_end__year'][i]), 
                    int(data['exp_end__month'][i]),
                    1
                )
            )
        edu_degrees = [key for key in data.keys() if key.startswith('edu_degrees')]
        for i in range(len(data['establishment'])):
            new_education = Education.objects.create(
                cv=cv,
                degree=data[edu_degrees[i]][0],
                establishment=data['establishment'][i],
                faculty=data['faculty'][i],
                specialization=data['specialization'][i],
                start_year=data['start_year_edu'][i],
                end_year=data['end_year_edu'][i]
            )
        return redirect(reverse('my-cv'))
    context = {
        'cv': cv
    }
    return render(request, 'employee/cv_edit.html', context)


class CVListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = CV
    ordering = ['-date_posted']

    def test_func(self):
        return hasattr(
            self.request.user, 'company') or hasattr(
            self.request.user, 'enterpreneuer')


@employee_required
@login_required
def delete_cv(request, id):
    try:
        cv = CV.objects.get(id=id)
    except Exception:
        return redirect(reverse('my-cv'))
    if cv.employee == request.user.employee:
        cv.delete()
    return redirect(reverse('my-cv'))
    

@api_view(('GET',))
@hirer_required
@login_required
def add_to_chosen(request, id):
    cv = CV.objects.get(id=id)
    if cv:
        try:
            chosen = ChosenCv.objects.get(hirer=request.user, cv=cv)
        except Exception:
            chosen = None
        if not chosen:
            chosen = ChosenCv.objects.create(hirer=request.user, cv=cv)
        else:
            chosen.delete()
        return r(status=status.HTTP_202_ACCEPTED)
    return r(status=status.HTTP_404_NOT_FOUND)


@employee_required
@login_required
def get_contact(request, id):
    try:
        contact = ChosenContact.objects.filter(
            contact__pk=id,
            user=request.user
        )
    except Exception:
        contact = None
    if not contact:
        new_contact = ChosenContact.objects.create(
            contact__pk=id,
            user=request.user
        )
    else:
        contact.delete()
    return redirect(reverse('home'))


@employee_required
@login_required
def make_response(request, id):
    try:
        response = Response.objects.get(vacancy=id, employee=request.user.employee)
    except Exception:
        response = None
        vacancy = Vacancy.objects.get(id=id)
    if not response:
        response = Response.objects.create(
            vacancy=vacancy,
            employee=request.user.employee
        )
        print('Created!')
    else:
        response.delete()
        print('Deleted!')
    return redirect(request.META.get('HTTP_REFERER'))


@employee_required
@login_required
def my_cv(request):
    cv_list = CV.objects.filter(employee=request.user.employee)
    context = {
        'cv_list': cv_list
    }
    return render(request, 'employee/my_cv.html', context)


def get_cv(request, n):
    cv_list = CV.objects.all()[n:n+20]
    serializer = CVSerializer(cv_list, many=True)
    data = [dict(i) for i in list(serializer.data)]
    return JsonResponse(data, safe=False, status=201)


class MyCVDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = CV
    template_name = 'employee/my_cv_detail.html'

    def test_func(self):
        if not hasattr(self.request.user, 'employee'):
            return False
        cv = self.get_object()
        return cv.employee == self.request.user.employee


class CVDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = CV
    template_name = 'employee/cv_detail.html'


    def get(self, request, *args, **kwargs):
        cv = self.get_object()
        cv.views += 1
        cv.save()
        return super().get(request, *args, **kwargs)


    def test_func(self):
        return hasattr(self.request.user, 'hirer')


def refresh_cv(request, id):
    try:
        cv = CV.objects.get(id=id)
    except Exception:
        cv = None
    if cv:
        cv.creation_date = tz.now()
        cv.save()
    return redirect(request.META.get('HTTP_REFERER'))


@hirer_required
@login_required
def chosen_cvs(request):
    cv_list = [chosen.cv for chosen in request.user.chosencv_set.all()]
    articles = favourite_articles(request)
    context = {
        'cv_list': cv_list,
        'articles': articles,
    }
    return render(request, 'employee/chosen.html', context)


@hirer_required
@login_required
def suitable_cvs(request, id):
    vacancy = Vacancy.objects.get(id=id)
    context = {
        'cv_list': vacancy.cv_set.all()
    }
    return render(request, 'employee/suitable_cvs.html', context)


@hirer_required
@login_required
def vacancy_responses(request, id):
    try:
        responses = Response.objects.filter(vacancy__id=id)
    except Exception:
        print('error!')
        responses = []
    context = {
        'responses': responses
    }
    return render(request, 'employee/')


@employee_required
@login_required
def my_responses(request):
    responses = Response.objects.filter(employee=request.user.employee)
    context = {
        'responses': responses,
    }
    return render(request, 'employee/my_responses.html', context)