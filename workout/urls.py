from django.urls import path
from . import views

urlpatterns = [
	path('', views.workout, name="workout"),
    path("", views.index, name="index"),  # Page url
]

    