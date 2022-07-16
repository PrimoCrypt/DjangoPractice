from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("primo/", views.primo, name="primo"),
    path("<str:name>", views.greet, name="greet"),
]
