from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def login_view(request):
    stu_name = request.POST.get('username')
    stu_password = request.POST.get('password')
    if stu_name and stu_password:
        # StudentInfo是学生资料数据表的名字，字段名为下面两个紫色的字符串
        c = StudentInfo.objects.filter(stu_name=stu_name, stu_psw=stu_password).count()
        if c == 1 :
            return HttpResponse("登录成功")
        else:
            return HttpResponse("账号密码错误")
    else:
        return HttpResponse("账号密码不能为空")

def competition(request):
    return render(request, 'competition.html')

def lab(request):
    return render(request, 'lab.html')

def guide(request):
    return render(request, 'guide.html')