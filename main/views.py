from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from .utils import generate_token, get_user_type, get_data, get_footer
from .decorators import login_forbidden, hirer_required, employee_required
from .forms import (
    PhoneNumEditForm, EmailEditForm, 
    PasswordEditForm, SphereEditForm,
    CompNameEditForm, CityEditForm,
    LogoEditForm, FirstNameEditForm,
    LastNameEditForm
)


def home(request):
    if hasattr(request.user, 'employee'):
        suffix = '_employee'
        context = get_data('employee')
    elif hasattr(request.user, 'hirer'):
        suffix = '_hirer'
        context = get_data('hirer')
    else:
        suffix = ''
        context = get_data('employee')
    context.update(get_footer())
    return render(request, f'main/home{suffix}.html', context)


@login_forbidden
def reg_type(request):
    return render(request, 'main/reg_type.html')


@login_forbidden
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            messages.add_message(
                request, messages.ERROR, 'Invalid credentials')
            return render(request, 'main/login.html')
        login(request, user)
        return redirect(reverse('home'))
    return render(request, 'main/login.html')


def activate_user(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except Exception as e:
        user = None
    if user and generate_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.add_message(request, messages.SUCCESS, 'Email Verified')
        return redirect(reverse('login'))
    return render(request, 'main/activation_failed.html', {"user": user})


@login_required
def phone_num_edit(request):
    if request.method == 'POST':
        form = PhoneNumEditForm(request.POST)
        if form.is_valid():
            user = get_user_type(request.user)
            user.phone_num = form.cleaned_data.get('phone_num')
            user.save()
        return redirect(reverse('profile'))
    context = {
        'heading': 'номер телефона',
        'name': 'phone_num'
    }
    return render(request, 'main/edit.html', context)


@login_required
def password_edit(request):
    if request.method == 'POST':
        form = PasswordEditForm(request.POST)
        if form.is_valid():
            request.user.set_password(form.cleaned_data.get('password'))
            request.user.save()
        return redirect(reverse('profile'))
    context = {
        'heading': 'пароль',
        'name': 'password'
    }
    return render(request, 'main/edit.html', context)


@login_required
def company_name_edit(request):
    if request.method == 'POST':
        form = CompNameEditForm(request.POST)
        if form.is_valid():
            request.user.hirer.company_name = form.cleaned_data.get(
                'company_name'
            )
            request.user.hirer.save()
        return redirect(reverse('profile'))
    context = {
        'heading': 'название компании',
        'name': 'company_name'
    }
    return render(request, 'main/edit.html', context)


@employee_required
@login_required
def first_name_edit(request):
    if request.method == 'POST':
        form = FirstNameEditForm(request.POST)
        if form.is_valid():
            request.user.employee.first_name = form.cleaned_data.get(
                'first_name'
            )
            request.user.employee.save()
        return redirect(reverse('profile'))
    context = {
        'heading': 'Имя',
        'name': 'first_name'
    }
    return render(request, 'main/edit.html', context)


@employee_required
@login_required
def last_name_edit(request):
    if request.method == 'POST':
        form = LastNameEditForm(request.POST)
        if form.is_valid():
            request.user.employee.last_name = form.cleaned_data.get(
                'last_name'
            )
            request.user.employee.save()
        return redirect(reverse('profile'))
    context = {
        'heading': 'Фамилия',
        'name': 'last_name'
    }
    return render(request, 'main/edit.html', context)


@hirer_required
@login_required
def sphere_edit(request):
    if request.method == 'POST':
        form = SphereEditForm(request.POST)
        if form.is_valid():
            request.user.hirer.sphere = form.cleaned_data.get('sphere')
            request.user.hirer.save()
        return redirect(reverse('profile'))
    context = {
        'heading': 'пароль',
        'name': 'sphere'
    }
    return render(request, 'main/edit.html', context)


@login_required
def city_edit(request):
    if request.method == 'POST':
        form = CityEditForm(request.POST)
        if form.is_valid():
            user = get_user_type(request.user)
            user.city = form.cleaned_data.get('city')
            user.save()
        return redirect(reverse('profile'))
    context = {
        'heading': 'город',
        'name': 'city'
    }
    return render(request, 'main/edit.html', context)


@hirer_required
@login_required
def logo_edit(request):
    if not hasattr(request.user.hirer, 'enterpreneuer'):
        return redirect(request.META.get('HTTP_REFERER'))
    enterpreneuer = request.user.hirer.enterpreneuer
    if request.POST:
        form = LogoEditForm(request.POST, request.FILES)
        if form.is_valid():
            print('Valid')
            enterpreneuer.logo.delete(save=True)
            enterpreneuer.logo = form.cleaned_data.get('logo')
            enterpreneuer.save()
        print(form.errors)
        return redirect(reverse('profile'))
    return render(request, 'main/edit_logo.html')


@login_forbidden
def activate_message(request):
    return render(request, 'main/activation_message.html')


@login_required
def profile(request):
    if hasattr(request.user, 'employee'): prefix = 'employee'
    elif hasattr(request.user, 'hirer'): prefix = 'hirer'
    return render(request, f'main/{prefix}_profile.html')


@login_required
def delete_user(request):
    user = request.user
    logout(request)
    user.delete()
    return redirect(reverse('home'))