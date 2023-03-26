"""helpdesk_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from helpdesk.views import (
    ticket_list,
    new_ticket,
    MyLoginView,
    ticket_detail,
    delete_ticket,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("tickets/", ticket_list, name="ticket_list"),
    path("new_ticket/", new_ticket, name="new_ticket"),
    path("accounts/login/", MyLoginView.as_view(), name="login"),
    path("tickets/<int:ticket_id>/", ticket_detail, name="ticket_detail"),
    path("tickets/<int:ticket_id>/delete/", delete_ticket, name="delete_ticket"),
]
