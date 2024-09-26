"""
URL configuration for NetSecLab project.

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
from django.urls import path
from More_apps.authen import views as auth_views
urlpatterns = [
    path("admin/", admin.site.urls),
    path('', auth_views.home, name='home'),  # 首页
    path('tologin/', auth_views.tologin_view, name='tologin'),  # 登录页面
    path('tologin/login',auth_views.login_view, name='login'),#账号密码输入后的跳转页面
    path('competition/', auth_views.competition, name='competition'),  # 竞赛公示
    path('lab/', auth_views.lab, name='lab'),  # 实验室公示
    path('guide/', auth_views.guide, name='guide'),  # 使用指南
    path('register/student/', views.register_student, name='student_register'),
    path('register/teacher/', views.register_teacher, name='teacher_register'),
    path('success/', views.success, name='success'),
path('teacher_home/', views.teacher_home, name='teacher_home'),
path('student_home/', views.student_home, name='student_home'),
]
