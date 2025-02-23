"""
URL configuration for Event_Management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from Event.views import AddEvent,EventDetails,EventUpdate,EventDelete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/',AddEvent.as_view()),
    path('info/',EventDetails.as_view()),
    path('update/<int:pk>',EventUpdate.as_view()),
    path('delete/<int:pk>',EventDelete.as_view()),
]
