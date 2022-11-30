
from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [

    # path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('', views.projects, name='projects'),
    path('contact', views.contact, name='contact'),
    path('service/<str:pk>', views.service, name='service'),
]
