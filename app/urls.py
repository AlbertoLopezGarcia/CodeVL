from django.urls import path
from app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:function>', views.home, name='enter_text'),
]