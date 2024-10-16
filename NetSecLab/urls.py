"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import authenticate
from django.urls import path, include, re_path
from django.views.generic import TemplateView

from More_apps.authen import views
from More_apps.authen.views import register_user
from More_apps.competition_student.views import student_info_api
from More_apps.competition_teacher import urls as teacher_urls
from More_apps.competition_student import urls as student_urls
from More_apps.competition_teacher.views import teacher_info

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # 首页
    path('login/', views.login_view, name='login'),  # 登录页面
    path('competition/', views.competition, name='competition'),  # 竞赛公示
    path('lab/', views.lab, name='lab'),  # 实验室公示
    path('guide/', views.guide, name='guide'),  # 使用指南
path('api/register/', register_user, name='register_user'),
    path('success/', views.success, name='success'),

path('student/',include(student_urls)),
path('teacher/',include(teacher_urls)), # 将所有以app2开头的urls，都交给app2(app名)下的urls.py处理
re_path(r'^$', TemplateView.as_view(template_name='index.html')),
path('api/student-info/', student_info_api, name='student_info_api'),
    path('api/teacher-info/', teacher_info, name='teacher_info'),
]
