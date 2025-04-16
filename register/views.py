from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.cache import cache_control
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash
from .forms import newuserform, userprofileupdateform
from django.contrib import messages

# Create your views here.


# Registretion
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def register_request(request):
    if request.method == "POST":
        form = newuserform(request.POST)
        if form.is_valid():
            user = form.save()
            print("User created:", user)  # Creation of the user
            messages.success(request, f"User has been Created. Welcome to GODHOOD!")
            login(request, user)
            return redirect("/workout")
        else:
            print(" Errors:", form.errors)  # Error in the creation of the user
    else:
        form = newuserform()
    return render(request, "register/register.html", {"register_form": form})


# Login
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login_request (request):
    if request.user.is_authenticated:
        return redirect("/workout")

    if request.method == "POST":
        form = AuthenticationForm (request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get ('username')
            password = form.cleaned_data.get ('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Welcome {username}!!")
                return redirect("/workout")
            else: 
                messages.error(request, "Invalid username or password.")
    else: 
        form = AuthenticationForm()
    return render(request, "register/login.html", {"login_form": form})

# Logout
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout_request (request):
    logout(request)
    request.session.flush()  # Clears data
    messages.success(request, "You have logged out. The GODS look down upon you!!")
    return redirect("/login")




# User profile
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def profile(request):
    return render(request, 'register/profile.html', {'user': request.user})




# Updating user information (username, email, password)
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required
def update_profile(request):
    if request.method == 'POST':
        form = userprofileupdateform(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            new_password = form.cleaned_data.get('password') # Password update only if the field is not empty
            if new_password:  # Update the password if there is one
                user.set_password(new_password)
            user.save()
            update_session_auth_hash(request, user)  # User is logged in after password change
            messages.success(request, 'Profile has been updated successfully!')
            return redirect('profile')
        else:
            messages.error(request, 'You have made an error make a correction below.')
    else:
        form = userprofileupdateform(instance=request.user)
    return render(request, 'register/update_profile.html', {'form': form})