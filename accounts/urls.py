from django.urls import path
from . import views

urlpatterns = [
    path('',views.login,name='login'),
    path('change-password/', views.change_admin_password, name='change_admin_password'),
]
