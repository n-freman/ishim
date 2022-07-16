from django.urls import path
from . import views

urlpatterns = [
    path('get/<id>', views.get_contact, name='get-contact'),
    path('get-by-vac/<int:id>', views.get_by_vac, name='get-by-vac'),
    path('saved', views.saved, name='saved-contacts'),
]