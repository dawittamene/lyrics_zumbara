from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name="index"),
    path('pictures/', views.pictures, name="pictures"),
    path('video/', views.video, name="video")
]
