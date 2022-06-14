from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('news/', views.news, name='news'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('exchange/', views.exchange, name='exchange'),
    path('contact/', views.contact, name='contact'),

]