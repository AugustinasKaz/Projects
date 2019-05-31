from django.urls import path
from . import views

urlpatterns = [
    path("", views.start),
    path("login/", views.index, name="index"),
    path("auth/", views.auth),
]