from django.shortcuts import render

# Create your views here.
def guide(request):
    return render(request, 'guide.html')

def question1(request):
    return render(request, 'question1.html')

def question2(request):
    return render(request, 'question2.html')

def question3(request):
    return render(request, 'question3.html')

def question4(request):
    return render(request, 'question4.html')

def consult(request):
    return render(request, 'consult.html')

def feedback(request):
    return render(request, 'feedback.html')