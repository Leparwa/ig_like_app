from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# @login_required(login_url='/accounts/login/')
def home(request):
    return render(request, 'ig/home.html')

