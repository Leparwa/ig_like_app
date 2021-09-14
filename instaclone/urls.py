from django.urls import path, include
from django_registration.backends.one_step.views import RegistrationView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("profile/", views.profile, name="profile"),
    path("register/", views.register, name="register"),
    path("edit-profile/", views.update_profile, name="edit-profile"),
    path('accounts/', include('django.contrib.auth.urls')),
    ]