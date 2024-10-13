from django.urls import path

from . import views

urlpatterns = [
    path("categories", views.get_password_categories),
    path("categories/<uuid:id>", views.get_password_category_by_id),
    path("categories", views.create_password_category),
    path("categories/<uuid:id>", views.update_password_category),
    path("categories/<uuid:id>", views.delete_password_category),
    path("", views.get_passwords),
    path("<uuid:id>", views.get_password_by_id),
    path("", views.create_password),
    path("<uuid:id>", views.update_password),
    path("<uuid:id>", views.delete_password),
]
