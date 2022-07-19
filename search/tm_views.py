from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from main.decorators import employee_required, hirer_required
from main.utils import get_footer
from vacancy.models import Vacancy
from employee.models import CV
from django.db.models import CharField
from django.db.models.functions import Lower
from .models import Story

CharField.register_lookup(Lower)


@hirer_required
@login_required
def search_cv(request):
    try:
        position = dict(request.GET)['position'][0]
        if not position:
            position = dict(request.GET)['position'][1]
    except Exception:
        print('ERROR!')
        position = ''
    cvs = list(CV.objects.filter(
        position__contains=position)
    )
    context = {
        'cv_list': cvs,
    }
    context.update(get_footer())
    return render(request, 'tm_search/search_cv_results.html', context)


@employee_required
@login_required
def search_vacancy(request):
    try:
        position = dict(request.GET)['position'][0]
        if not position:
            position = dict(request.GET)['position'][1]
    except Exception:
        print('ERROR!')
        position = ''
    vacancies = list(
        Vacancy.objects.filter(
            position__contains=position)
    )
    context = {
        'vacancies': vacancies
    }
    context.update(get_footer())
    return render(request, 'tm_search/search_vacancy_results.html', context)


@hirer_required
@login_required
def wide_search_cv(request):
    if request.POST:
        data = dict(request.POST)
        if data['position'] and data['sphere']:
            print('Here...')
            cvs = list(
                CV.objects.filter(
                    position__contains=data['position'][0],
                    sphere__contains=data['sphere'][0]
                )
            )
            context = {
                'cv_list': cvs,
            }
            del data['csrfmiddlewaretoken']
            Story.objects.create(
                user=request.user,
                search=data
            )
            context.update(get_footer())
            return render(request, 'tm_search/search_cv_results.html', context)
    return render(request, 'tm_search/wide_search_cv.html', get_footer())


@employee_required
@login_required
def wide_search_vacancy(request):
    if request.POST:
        data = dict(request.POST)
        if data['position'] and data['sphere']:
            vacancies = list(
                Vacancy.objects.filter(
                    position__contains=data['position'][0],
                    sphere__contains=data['sphere'][0]
                    )
            )
            context = {
                'vacancies': vacancies
            }
            del data['csrfmiddlewaretoken']
            Story.objects.create(
                user=request.user,
                search=data
            )
            context.update(get_footer())
            return render(request, 'tm_search/search_vacancy_results.html', context)
    return render(request, 'tm_search/wide_search_vacancy.html', get_footer())


@employee_required
@login_required
def search_history_employee(request):
    stories = Story.objects.filter(user=request.user)
    context = {
        'stories': stories
    }
    return render(request, 'tm_search/search_history_employee.html', context)


@hirer_required
@login_required
def search_history_hirer(request):
    stories = Story.objects.filter(user=request.user)
    context = {
        'stories': stories
    }
    for story in stories:
        print(story.search)
    return render(request, 'tm_search/search_history_hirer.html', context)


@login_required
def delete_history(request, id):
    story = Story.objects.get(id=id)
    if request.user == story.user:
        story.delete()
    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def clear_hisory(request):
    user = request.user
    user.story_set.all().delete()
    return redirect(request.META.get('HTTP_REFERER'))


@login_required
def search_again(request, id):
    story = Story.objects.get(id=id)
    if hasattr(request.user, 'employee'):
        vacancies = Vacancy.objects.filter(
            position__contains=story.search.position,
            sphere__contains=story.search.sphere
            )
        context = {
            'vacancies': vacancies
        }
        return render(request, 'tm_search/search_vacancy_results.html', context)
    else:
        cv_list = CV.objects.filter(
            position__contains=story.search.position,
            sphere__contains=story.search.sphere
        )
        context = {
            'cvs': cv_list
        }
        return render(request, 'tm_search/search_cv_results.html', context)
    
