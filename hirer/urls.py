from django.urls import path
from . import views

urlpatterns = [
    path('register/company', views.company_create, name='create-company'),
    path('register/enterpreneuer', views.enterpreneuer_create, name='create-enterpreneuer'),
    path('type', views.hirer_type, name='hirer-type'),
    path('all-companies/', views.company_catalog, name='company-catalog'),
    path('by-sphere/<str:sphere>', views.companies_by_sphere, name='companies-by-sphere'),
    # path('hirer-info/<int:id>/', views.hirer_info, name='hirer-info'),
]