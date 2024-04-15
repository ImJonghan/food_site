from django.urls import path, include
from . import views
urlpatterns = [
    path("add_food/", views.add_food, name='add_food'),
]
