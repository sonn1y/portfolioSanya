from django.urls import path
from blog_01 import views

urlpatterns = [
    path("", views.home, name="home"),
]