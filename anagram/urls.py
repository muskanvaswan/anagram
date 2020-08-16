from django.urls import path
from . import views

urlpatterns = [
    path("", views.ana, name="anagram"),
    path("anagram/result", views.solution, name="solve")
]
