from django.urls import path

from . import views

urlpatterns = [
    path("login", views.login),
    path("sign-up", views.sign_up),
    path("profile", views.get_profile_information),
]
