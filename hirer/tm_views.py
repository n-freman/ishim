from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Count, F
from employee.forms import UserCreateForm
from main.decorators import login_forbidden, hirer_required, employee_required
from main.utils import send_activation_email
from vacancy.models import Vacancy
from .forms import *
from .models import Hirer


@login_forbidden
def company_create(request, *args):
    if request.method == 'POST':
        u_form = UserCreateForm(request.POST)
        c_form = CompanyCreateForm(request.POST)
        print(u_form.errors)
        print(c_form.errors)
        if u_form.is_valid() and c_form.is_valid():

            try:
                if User.objects.get(email=request.POST.get('email')):
                    messages.add_message(request, messages.ERROR, 'User with this email already exists')
                    u_form = UserCreateForm()
                    e_form = EmployeeCreateForm()
                    context = {
                        'u_form': u_form,
                        'e_form': e_form,
                    }
                    return render(request, 'tm_hirer/company_create.html', context)

            except Exception as identifier:
                print(identifier)
            
            user = u_form.save(commit=False)
            user.username = user.email
            user.is_active = False
            user.save()
            company = c_form.save(commit=False)
            company.user = user
            company.save()
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
                return redirect(reverse('activate-message-tm'))
    return render(request, 'hirer/company_create.html')


@login_forbidden
def enterpreneuer_create(request, *args):
    if request.method == 'POST':
        print(request.POST)
        u_form = UserCreateForm(request.POST)
        e_form = EnterpreneuerCreateForm(request.POST, request.FILES)
        if u_form.is_valid() and e_form.is_valid():

            try:
                if User.objects.get(email=request.POST.get('email')):
                    messages.add_message(request, messages.ERROR, 'User with this email already exists')
                    u_form = UserCreateForm()
                    e_form = EmployeeCreateForm()
                    context = {
                        'u_form': u_form,
                        'e_form': e_form,
                    }
                    return render(request, 'tm_hirer/enterpreneuer_create.html', context)

            except Exception as identifier:
                print(identifier)

            user = u_form.save(commit=False)
            user.username = user.email
            user.is_active = False
            user.save()
            enterpreneuer = e_form.save(commit=False)
            enterpreneuer.user = user
            enterpreneuer.save()
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
            print('One of the forms is unvalid')
    return render(request, 'hirer/enterpreneuer_create.html')


@login_forbidden
def hirer_type(request):
    return render(request, 'tm_hirer/hirer_type.html')


@login_required
def company_catalog(request):
    context = {}
    context['spheres'] = list(Hirer.objects.values('sphere').annotate(dcount=Count('sphere')).order_by())
    context['hirers'] = Hirer.objects.all()
    print(context)
    return render(request, 'tm_hirer/company_catalog.html', context)


@login_required
def companies_by_sphere(request, sphere):
    companies = Hirer.objects.filter(sphere=sphere)
    return render(request, 'tm_hirer/companies_by_sphere.html', {'companies': companies, 'sphere': sphere})



# @login_required
# def hirer_info(request, id):
#     context = {
#         'hirer': Hirer.objects.get(id=id)
#     }
#     return render(request, 'hirer/hirer_info.html', context)