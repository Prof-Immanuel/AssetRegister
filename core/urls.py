from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("register/", views.item_register, name="item_register"),
    path('report-item', views.report, name='report'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('success/', views.success, name='success'),
    path('error/', views.error, name='error'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
