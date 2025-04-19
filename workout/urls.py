from django.urls import path
from . import views
from .views import workout_list, create_workout, vote_workout

urlpatterns = [
	path("", views.index, name="index"), 
    path('workout_list/', workout_list, name='workout_list'),
    path('create_workout/', create_workout, name='create_workout'),
    path('vote/<int:workout_id>/<str:vote_type>/', vote_workout, name='vote_workout'),# for the votes


    path('staff-portal/', views.staff_portal, name='staff_portal'),# for staff

    path('questions/', views.question_list, name='question_list'),#questions
    path('questions/ask/', views.ask_question, name='ask_question'),
    path('questions/<int:pk>/answer/', views.answer_question, name='answer_question'),

    path('staff/workouts/', views.manage_workouts, name='manage_workouts'),# workouts
    path('staff/workouts/<int:pk>/edit/', views.edit_workout, name='edit_workout'),
    path('staff/workouts/<int:pk>/delete/', views.delete_workout, name='delete_workout'),


    path('staff/exercises/', views.manage_exercises, name='manage_exercises'),# exercises
    path('staff/exercises/<int:pk>/edit/', views.edit_exercise, name='edit_exercise'),
    path('staff/exercises/<int:pk>/delete/', views.delete_exercise, name='delete_exercise'),
    path('staff/exercises/create/', views.create_exercise, name='create_exercise'),
]

    