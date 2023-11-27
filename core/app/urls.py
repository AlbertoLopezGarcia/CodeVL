from django.urls import path
from app import views

urlpatterns = [
    path('enter_text/', views.enter_text, name='enter_text'),
    path('enter_text/<str:function>', views.enter_text, name='enter_text'),
]