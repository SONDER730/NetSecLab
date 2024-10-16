# Generated by Django 5.1.1 on 2024-10-16 09:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('competition_student', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('teacher_id', models.CharField(max_length=20, unique=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=10)),
                ('contact', models.CharField(max_length=15)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CompetitionApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('pending', '审核中'), ('approved', '进行中'), ('rejected', '已拒绝')], default='pending', max_length=20)),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competition_student.competition')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competition_student.studentinformation')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competition_teacher.teacherinformation')),
            ],
        ),
    ]
