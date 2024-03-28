# core/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # CRUD Views for the Item model
    path("", views.list_items, name="list_items"),
    path("create/", views.create_item, name="create_item"),
    path("update/<int:pk>/", views.update_item, name="update_item"),
    path("delete/<int:pk>/", views.delete_item, name="delete_item"),
    # Privacy Policy, Impressum, About and Contact for the sake of completeness
    path("privacy_policy", views.privacy_policy, name="privacy_policy"),
    path("impressum", views.impressum, name="impressum"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
]
