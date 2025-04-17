from django.urls import path
from . import views
from .views import workout_list, create_workout, like_workout, dislike_workout, vote_workout

urlpatterns = [
	path("", views.index, name="index"), 
    path('workout_list/', workout_list, name='workout_list'),
    path('create_workout/', create_workout, name='create_workout'),
    path('like/<int:workout_id>/', like_workout, name='like_workout'),
    path('dislike/<int:workout_id>/', dislike_workout, name='dislike_workout'),
    path('vote/<int:workout_id>/<str:vote_type>/', vote_workout, name='vote_workout'),
]

    