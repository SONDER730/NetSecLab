# Generated by Django 5.1.1 on 2024-10-13 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authen', '0003_alter_studentinfo_student_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentinfo',
            name='name',
        ),
        migrations.RemoveField(
            model_name='teacherinfo',
            name='name',
        ),
    ]