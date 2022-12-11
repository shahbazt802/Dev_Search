
from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [

    # path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('', views.projects, name='projects'),
    # path('', views.navbar1, name='navbar1'),
    path('project/<str:pk>', views.project, name='project'),
    path('service/<str:pk>', views.service, name='service'),
    path('create-project', views.createProject, name='create-project'),
    path('update-project/<str:pk>', views.updateProject, name='update-project'),
    path('delete-project/<str:pk>', views.deleteProject, name='delete-project'),
]
