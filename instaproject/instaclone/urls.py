from django.urls import path, include
from django_registration.backends.one_step.views import RegistrationView
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('accounts/register', RegistrationView.as_view(success_url='home/'), name='django_registration_register'),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    ]