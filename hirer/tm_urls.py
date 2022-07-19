from django.urls import path
from . import tm_views

urlpatterns = [
    path('register/company', tm_views.company_create, name='create-company-tm'),
    path('register/enterpreneuer', tm_views.enterpreneuer_create, name='create-enterpreneuer-tm'),
    path('type', tm_views.hirer_type, name='hirer-type-tm'),
    path('all-companies/', tm_views.company_catalog, name='company-catalog-tm'),
    path('by-sphere/<str:sphere>', tm_views.companies_by_sphere, name='companies-by-sphere-tm'),
    # path('hirer-info/<int:id>/', tm_views.hirer_info, name='hirer-info-tm'),
]