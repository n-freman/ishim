from django.urls import path
from . import views

urlpatterns = [
    path('get/<id>', views.get_contact, name='get-contact'),
    path('saved', views.saved, name='saved-contacts'),
]