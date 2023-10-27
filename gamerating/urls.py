from django.urls import path

from . import views

urlpatterns = [
    # ex: /gamerating/
    path("", views.index, name="index"),
    # ex: /gamerating/5/
    path("<int:game_id>/", views.detail, name="detail"),
]