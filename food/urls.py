from django.contrib import admin
from django.urls import path
from .views import FoodView

urlpatterns = [
    path('food/', FoodView.as_view()),
    path("food/<int:pk>/",FoodView.as_view())
]