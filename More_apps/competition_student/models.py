<<<<<<< HEAD
from django.db import models

class StudentInfo(models.Model):
    stu_name = models.CharField(max_length=100, verbose_name='姓名')
    stu_id = models.CharField(max_length=20, unique=True, verbose_name='学号')
    stu_password = models.CharField(max_length=128, verbose_name='密码')
    major = models.CharField(max_length=100, verbose_name='专业')

    def __str__(self):
        return self.stu_name

    class Meta:
        verbose_name = '学生信息'
        verbose_name_plural = '学生信息'
=======
from django.contrib.auth.models import User
from django.db import models

from More_apps.authen.models import StudentInfo, TeacherInfo


class StudentInformation(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=30)
    gender = models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    school = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    grade = models.CharField(max_length=10)


    def __str__(self):
        return self.name


class Competition(models.Model):
        name = models.CharField(max_length=100)
        description = models.TextField()
        start_date = models.DateField()
        end_date = models.DateField()

        def __str__(self):
            return self.name


class StudentFileUpload(models.Model):
    file = models.FileField(upload_to='student_uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    student = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.file.name} uploaded by {self.student.name}"
>>>>>>> 83f1edfc5ffa8e9f876eb602fbd78e4443d636dc
