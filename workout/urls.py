from django.urls import path
from . import views
from .views import workout_list, create_workout, vote_workout

urlpatterns = [
	path("", views.index, name="index"), 
    path('workout_list/', workout_list, name='workout_list'),
    path('create_workout/', create_workout, name='create_workout'),
    path('vote/<int:workout_id>/<str:vote_type>/', vote_workout, name='vote_workout'),
]

    