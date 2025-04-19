from django.urls import path
from . import views


urlpatterns = [
    path('my-sessions/', views.my_training_sessions, name='my_training_sessions'),
]