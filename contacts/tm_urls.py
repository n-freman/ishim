from django.urls import path
from . import tm_views

urlpatterns = [
    path('get/<id>', tm_views.get_contact, name='get-contact-tm'),
    path('get-by-vac/<int:id>', tm_views.get_by_vac, name='get-by-vac-tm'),
    path('saved', tm_views.saved, name='saved-contacts-tm'),
    path('get-by-cv/<int:id>', tm_views.get_by_cv, name='get-contact-by-cv-tm'),
    path('saved-cv/', tm_views.saved_cv_contacts, name='saved-cv-contacts-tm'),
]