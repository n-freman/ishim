"""ishim URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from main.views import (
    home, login_view, 
    activate_user, reg_type, 
    activate_message, profile,
    delete_user, password_edit,
    company_name_edit, phone_num_edit,
    sphere_edit, city_edit, 
    logo_edit, first_name_edit,
    last_name_edit
)

from main import tm_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('employee/', include('employee.urls')),
    path('hirer/', include('hirer.urls')),
    path('vacancy/', include('vacancy.urls')),
    path('articles/', include('articles.urls')),
    path('search/', include('search.urls')),
    path('contacts/', include('contacts.urls')),
    path('login/', login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(
            template_name='main/logout.html'
        ),
        name='logout'),
    path('activate-user/<uidb64>/<token>', activate_user, name='activate'),
    path('register/', reg_type, name='register'),
    path('message/', activate_message, name='activate-message'),
    path('profile/', profile, name='profile'),
    path('delete-me/', delete_user, name='delete-me'),
    path('edit/password', password_edit, name='edit-password'),
    path('edit/company-name', company_name_edit, name='edit-company'),
    path('edit/phone', phone_num_edit, name='edit-phone'),
    path('edit/sphere', sphere_edit, name='edit-sphere'),
    path('edit/city', city_edit, name='edit-city'),
    path('edit/first_name', first_name_edit, name='edit-first-name'),
    path('edit/last_name', last_name_edit, name='edit-last-name'),
    path('edit/logo', logo_edit, name='logo-edit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


tm_urlpatterns = [
    path('tm/', tm_views.home, name='home-tm'),
    path('tm/employee/', include('employee.tm_urls')),
    path('tm/hirer/', include('hirer.tm_urls')),
    path('tm/vacancy/', include('vacancy.tm_urls')),
    path('tm/articles/', include('articles.tm_urls')),
    path('tm/search/', include('search.tm_urls')),
    path('tm/contacts/', include('contacts.tm_urls')),
    path('tm/login/', tm_views.login_view, name='login-tm'),
    path('tm/logout/', auth_views.LogoutView.as_view(
            template_name='tm_main/logout.html'
        ),
        name='logout-tm'),
    path('tm/activate-user/<uidb64>/<token>', tm_views.activate_user, name='activate-tm'),
    path('tm/register/', tm_views.reg_type, name='register-tm'),
    path('tm/message/', tm_views.activate_message, name='activate-message-tm'),
    path('tm/profile/', tm_views.profile, name='profile-tm'),
    path('tm/delete-me/', tm_views.delete_user, name='delete-me-tm'),
    path('tm/edit/password', tm_views.password_edit, name='edit-password-tm'),
    path('tm/edit/company-name', tm_views.company_name_edit, name='edit-company-tm'),
    path('tm/edit/phone', tm_views.phone_num_edit, name='edit-phone-tm'),
    path('tm/edit/sphere', tm_views.sphere_edit, name='edit-sphere-tm'),
    path('tm/edit/city', tm_views.city_edit, name='edit-city-tm'),
    path('edit/first_name', tm_views.first_name_edit, name='edit-first-name-tm'),
    path('edit/last_name', tm_views.last_name_edit, name='edit-last-name-tm'),
    path('tm/edit/logo', tm_views.logo_edit, name='logo-edit-tm'),
]


urlpatterns.extend(tm_urlpatterns)

admin.site.site_header = 'ISHIM admin page'
admin.site.site_title = 'ISHIM'