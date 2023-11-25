from django.contrib import admin
from django.urls import path,include
from . import views

app_name = 'schoolapp'
urlpatterns = [
    path('',views.index,name='index') ,
    path('about', views.about,name='about'),
    path('login', views.login,name='login'),
    path('register', views.register,name='register'),
    path('application/', views.application,name='application'),

    path('apply/', views.person_create_view, name='person_add'),
    path('<int:pk>/', views.person_update_view, name='person_change'),

    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),  # AJAX

]