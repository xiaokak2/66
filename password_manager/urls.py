"""
URL configuration for password_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from passwords import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('add/', views.add_password, name='add_password'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('mimabook/', views.mimabook, name='mimabook'),
    path('delete/<int:id>/', views.delete_password, name='delete_password'),
    path('rect/<int:id>/', views.rect_password, name='rect_password'),
    path('rect_password', views.rect_password, name='rect_password'),
    path('index/', views.index, name='index'),
    path('zhang/', views.zhang, name='zhang'),
    path('add_jizhang/', views.add_jizhang, name='add_jizhang'),
    path('delete_zhang/<int:id>/', views.delete_zhang, name='delete_zhang'),
    path('notbook/', views.notebook_list, name='notbook_list'),
    path('notbook/new/', views.notebook_new, name='notbook_new'),
    path('notbook/<int:pk>/', views.notebook_detail, name='notbook_detail'),
    path('notbook/<int:pk>/edit/', views.notebook_edit, name='notbook_edit'),
    path('notbook/<int:pk>/delete/', views.notebook_delete, name='notbook_delete'),
    path('contacts/', views.contact_list, name='contact_list'),
    path('contacts/<int:pk>/', views.contact_detail, name='contact_detail'),
    path('contacts/new/', views.contact_create, name='contact_create'),
    path('contacts/<int:pk>/edit/', views.contact_update, name='contact_update'),
    path('contacts/<int:pk>/delete/', views.contact_delete, name='contact_delete'),
    path('addresses/', views.address_list, name='address_list'),
    path('addresses/new/', views.address_create, name='address_create'),
    path('addresses/<int:pk>/edit/', views.address_update, name='address_update'),
    path('addresses/<int:pk>/delete/', views.address_delete, name='address_delete'),
]