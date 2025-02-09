from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('receipt/', views.receipt, name='receipt'),
    path('org_add/', views.org_add, name='org_add'),
]
