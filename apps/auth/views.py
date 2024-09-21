from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def login_view(request):
    return render(request, 'login.html')

def competition(request):
    return render(request, 'competition.html')

def lab(request):
    return render(request, 'lab.html')

def guide(request):
    return render(request, 'guide.html')