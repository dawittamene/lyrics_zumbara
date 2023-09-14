from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="index"),
    path('pictures/', views.pictures, name="pictures"),
    path('video/', views.video, name="video"),
    path('signup/', views.signup, name="signup"),
    path('loginpage/', views.loginpage, name="loginpage"),
    path('logoutPage/', views.logoutPage, name="logoutPage"),
    
]




