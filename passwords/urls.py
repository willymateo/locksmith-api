from django.urls import path

from passwords.views import (
    PasswordCategoryDetailAPIView,
    PasswordCategoryListAPIView,
    PasswordDetailAPIView,
    PasswordListAPIView,
)

urlpatterns = [
    path("categories/<uuid:id>/", PasswordCategoryDetailAPIView.as_view()),
    path("categories/", PasswordCategoryListAPIView.as_view()),
    path("<uuid:id>/", PasswordDetailAPIView.as_view()),
    path("", PasswordListAPIView.as_view()),
]
