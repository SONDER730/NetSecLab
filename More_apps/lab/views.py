from django.shortcuts import render

# Create your views here.
def lab(request):
    return render(request, 'lab.html')

def class1(request):
    return render(request, 'class1.html')

def class2(request):
    return render(request, 'class2.html')

def class3(request):
    return render(request, 'class3.html')

def class4(request):
    return render(request, 'class4.html')