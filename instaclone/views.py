from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages
from .models import Image, Profile
from django.db import transaction
from django.forms import modelformset_factory
from .forms import CustomUserCreationForm, ImageForm, ProfileForm, UserForm, ProfileForm

@login_required(login_url='/accounts/login/')
def home(request):
    images= Image.objects.all()
    profiles = Profile.objects.all().exclude(user=request.user)
    return render(request, 'ig/home.html', context ={'images': images, 'profiles':profiles })

@login_required(login_url='/accounts/login/')
def profile(request):
    return render(request, 'ig/profile.html')

def register(request):
    if request.method == "GET":
        return render(request, "users/register.html",{"form": CustomUserCreationForm})
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
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
        elif profile_form.is_valid():
            profile_form.save() 
        return redirect('profile')

    profile_form = ProfileForm(instance=request.user.profile)
    user_form = UserForm(instance=request.user)
    return render(request, 'ig/edit-user.html', {'user_form': user_form, "profile_form": profile_form})

@login_required
def new_post(request):
    if request.method == 'POST':
        image_form = ImageForm(request.POST, request.FILES)
        if image_form.is_valid():
            form = image_form.save(commit=False)
            form.profile = request.user.profile
            form.save()
            return redirect('home')
    else:
        form = ImageForm()
    return render(request, 'ig/new-post.html', {'form': form})