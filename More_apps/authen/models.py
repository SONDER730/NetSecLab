<<<<<<< HEAD

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


=======
from django.db import models

# Create your models here.


from django.db import models

class StudentInfo(models.Model):
    student_id = models.CharField(max_length=20)  # 保留 student_id
    email = models.EmailField(max_length=100)  # 添加 email 字段
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.student_id



class TeacherInfo(models.Model):
    teacher_id = models.CharField(max_length=20)  # 保留 teacher_id
    email = models.EmailField(max_length=100)  # 添加 email 字段
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.teacher_id
>>>>>>> 83f1edfc5ffa8e9f876eb602fbd78e4443d636dc
