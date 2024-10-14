from django.urls import path

from . import views

urlpatterns = [
    path("categories/<uuid:id>", views.PasswordCategoryDetailAPIView.as_view()),
    path("categories", views.PasswordCategoryListAPIView.as_view()),
    path("<uuid:id>", views.PasswordDetailAPIView.as_view()),
    path("", views.PasswordListAPIView.as_view()),
]
