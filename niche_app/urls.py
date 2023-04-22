from django.urls import path
from niche_app import views

urlpatterns = [
    path("", views.home, name="home"),
]