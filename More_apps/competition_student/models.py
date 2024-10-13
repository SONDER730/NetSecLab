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
