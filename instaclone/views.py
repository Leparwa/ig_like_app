from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages
from .models import Image
from django.db import transaction
from .forms import CustomUserCreationForm, ImageForm, ProfileForm, UserForm, ProfileForm

@login_required(login_url='/accounts/login/')
def home(request):
    images= Image.objects.all()

    print(images)
    return render(request, 'ig/home.html', context ={'images': images })

@login_required(login_url='/accounts/login/')
def profile(request):
    return render(request, 'ig/profile.html')

def register(request):
    if request.method == "GET":
        return render(
            request, "users/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        return redirect(reverse("home"))

@login_required
@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('profile')
        else:
            messages.error(request, ('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
    return render(request, 'ig/edit-user.html', {
        'user_form': user_form,
    })

@login_required
def new_post(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        profile_form = ImageForm(request.POST, request.FILES)
        if profile_form.is_valid():
            form = profile_form.save(commit=False)
            form.profile = request.user.profile
            form.save()
            return redirect('home')
    else:
        form = ImageForm()
    return render(request, 'ig/new-post.html', {'form': form})