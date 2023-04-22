from django.urls import path
from niche_app import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path("", views.home, name="home"),
]

urlpatterns += staticfiles_urlpatterns()