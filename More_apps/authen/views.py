from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from More_apps.authen.models import *


# Create your views here.



def home(request):
    return render(request, 'home.html')

def tologin_view(request):
    return render(request, 'tologin.html')

def login_view(request):
    stu_name = request.POST.get('username')
    stu_password = request.POST.get('password')
    if stu_name and stu_password:
        # StudentInfo是学生资料数据表的名字，字段名为下面两个紫色的字符串
        c = StudentInfo.objects.filter(stu_name=stu_name, stu_password=stu_password).count()
        if c == 1 :
            return HttpResponse("登录成功")
        else:
            return HttpResponse("账号密码错误")
    else:
        return HttpResponse("账号密码不能为空")

def competition(request):
    return render(request, 'competition.html')


def register_student(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.password = make_password(form.cleaned_data['password'])  # 密码加密
            student.save()
            messages.success(request, '学生注册成功！')
            return redirect('login')  # 重定向到登录页面
    else:
        form = StudentRegistrationForm()

    return render(request, 'student_register.html', {'form': form})


def register_teacher(request):
    if request.method == 'POST':
        form = TeacherRegistrationForm(request.POST)
        if form.is_valid():
            teacher = form.save(commit=False)
            teacher.password = make_password(form.cleaned_data['password'])  # 密码加密
            teacher.save()
            messages.success(request, '教师注册成功！')
            return redirect('login')  # 重定向到登录页面
    else:
        form = TeacherRegistrationForm()

    return render(request, 'teacher_register.html', {'form': form})
def success(request):
    return render(request, 'success.html')
def student_home(request):
    return render(request, 'student_home.html')
def teacher_home(request):
    return render(request, 'teacher_home.html')