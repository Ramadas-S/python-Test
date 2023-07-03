from django.urls import path
from . import views

urlpatterns = [
    # path('',views.login,name='login'),
    path('', views.login_account, name='login'),
    path('change-password/', views.change_admin_password, name='change_admin_password'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
