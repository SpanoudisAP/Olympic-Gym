from django.shortcuts import render
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages

# Create your views here.


#Homepage view
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):
    return render(request, 'home.html')


#Index/Workout page view
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def index(request):
    return render(request, 'workout/index.html')

#Workout view
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def workout(request):
    return render(request, 'workout.html' )


# Here starts the staff stuff :)

def staff_required(user):
    return user.is_staff


#Staff portal view
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@user_passes_test(staff_required)
def staff_portal(request):
    return render(request, 'staff/portal.html')