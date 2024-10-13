
from django.db import models

# 学生模型
class StudentInfo(models.Model):
    stu_name = models.CharField(max_length=50)  # 学生姓名
    stu_id = models.CharField(max_length=20, unique=True)  # 学号
    stu_password = models.CharField(max_length=50)  # 学生密码
    major = models.CharField(max_length=100)  # 专业



# 教师模型
class TeacherInfo(models.Model):
    tea_name = models.CharField(max_length=50)  # 教师姓名
    tea_id = models.CharField(max_length=20, unique=True)  # 工号
    tea_password = models.CharField(max_length=50)  # 教师密码


