from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('report-item', views.report, name='report'),
    path('success/', views.success, name='success'),
    path('error/', views.error, name='error'),
]
