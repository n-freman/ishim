from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from main.decorators import employee_required
from vacancy.models import Vacancy
from .models import Contact, ChosenContact


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