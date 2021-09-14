from django.contrib.auth.models import User 
from django import forms
from django.db.models import fields
from .models import Image, Profile
from django.contrib.auth.forms import UserCreationForm
from django.forms import widgets


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email", )
        
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email')
        
        widgets={
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),

        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model= Profile
        fields = ('bio', 'profile_photo')

        widgets={
            'bio':forms.TextInput(attrs={'class':'form-control'}),
            'profile_photo':forms.FileInput(attrs={'class':'form-control'}),
        }
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image','caption', 'name')
        
        widgets={
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'caption': forms.TextInput(attrs={'class':'form-control'}),
            'image': forms.FileInput(attrs={'class':'form-control'}),

        }