from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from main.decorators import employee_required, hirer_required
from vacancy.models import Vacancy
from employee.models import CV
from .models import Contact, ChosenContact, ChosenCVContact


@employee_required
@login_required
def get_contact(request, id):
    contact = Contact.objects.get(id=id)
    try:
        chosen = ChosenContact.objects.get(
            user=request.user,
            contact=contact
        )
    except Exception:
        chosen = None
    if not chosen:
        chosen = chosen = ChosenContact.objects.create(
            user=request.user,
            contact=contact
        )
    else:
        chosen.delete()
    return redirect(request.META.get('HTTP_REFERER'))


@employee_required
@login_required
def saved(request):
    contacts = [saved.contact for saved in request.user.chosencontact_set.all()]
    context = {
        'contacts': contacts
    }
    return render(request, 'contacts/saved.html', context)


@employee_required
@login_required
def get_by_vac(reqeuest, id):
    contact = Vacancy.objects.get(id=id).contact
    try:
        chosen = ChosenContact.objects.get(
            user=request.user,
            contact=contact
        )
    except Exception:
        chosen = None
    if not chosen:
        chosen = chosen = ChosenContact.objects.create(
            user=request.user,
            contact=contact
        )
    else:
        chosen.delete()
    return redirect(request.META.get('HTTP_REFERER'))


@hirer_required
@login_required
def get_by_cv(request, id):
    cv = get_object_or_404(CV, id=id)
    try:
        contact = ChosenCVContact.objects.get(
            cv=cv,
            user=request.user
        )
    except:
        contact = None
    if contact:
        contact.delete()
    else:
        data = cv.first_name + ' ' + cv.last_name + '\n' + cv.mobile_num + '\n' + cv.email
        contact = ChosenCVContact.objects.create(
            user=request.user,
            cv=cv,
            data=data
        )
    return redirect(request.META.get('HTTP_REFERER'))


@hirer_required
@login_required
def saved_cv_contacts(request):
    contacts = request.user.cv_contacts.all()
    context = {
        'contacts': contacts
    }
    return render(request, 'contacts/saved_cv.html', context)