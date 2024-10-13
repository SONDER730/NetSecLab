from django.db import models

class TeacherInfo(models.Model):
    tea_name = models.CharField(max_length=100, verbose_name='姓名')
    tea_id = models.CharField(max_length=20, unique=True, verbose_name='工号')
    tea_password = models.CharField(max_length=128, verbose_name='密码')

    def __str__(self):
        return self.tea_name

    class Meta:
        verbose_name = '教师信息'
        verbose_name_plural = '教师信息'
