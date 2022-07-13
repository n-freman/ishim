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
    logo_edit
)

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
    path('edit/logo', logo_edit, name='logo-edit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = 'ISHIM admin page'
admin.site.site_title = 'ISHIM'