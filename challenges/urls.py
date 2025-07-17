from django.urls import path

from . import views

urlpatterns = [
    path("january", views.jan),
    path("february", views.feb),
    path("march", views.mar),
    path("april", views.apr),
]