<<<<<<< HEAD
from myapp.oauth.models import StudentInfo, TeacherInfo
from django import forms
class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = StudentInfo
        fields = ['name', 'student_id', 'password', 'major']
        widgets = {
            'password': forms.PasswordInput(),
        }

class TeacherRegistrationForm(forms.ModelForm):
    class Meta:
        model = TeacherInfo
        fields = ['name', 'teacher_id', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

class LoginForm(forms.Form):
            user_id = forms.CharField(label='User ID', max_length=20)
            password = forms.CharField(widget=forms.PasswordInput())
            user_type = forms.ChoiceField(choices=[('student', 'Student'), ('teacher', 'Teacher')],
                                          widget=forms.RadioSelect)
=======
from django import forms
from .models import StudentInfo, TeacherInfo
import re
from django.core.exceptions import ValidationError

class StudentRegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label="确认密码", required=False)  # 设置 confirm_password 不必填

    class Meta:
        model = StudentInfo
        fields = ['student_id', 'email', 'password']  # 使用 student_id
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not (re.search('[A-Z]', password) and re.search('[a-z]', password) and
                re.search('[0-9]', password) and re.search('[^A-Za-z0-9]', password)):
            raise ValidationError("密码必须包含大写字母、小写字母、数字和特殊字符。")
        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = self.data.get("confirm_password")  # 使用 self.data.get 从请求中获取 confirm_password

        if password and confirm_password and password != confirm_password:
            raise ValidationError("两次输入的密码不一致。")
        return cleaned_data



from django import forms
from .models import TeacherInfo
from django.core.exceptions import ValidationError
import re

class TeacherRegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label="确认密码", required=False)  # 设置 confirm_password 不必填

    class Meta:
        model = TeacherInfo
        fields = ['teacher_id', 'email', 'password']  # 使用 teacher_id
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not (re.search('[A-Z]', password) and re.search('[a-z]', password) and
                re.search('[0-9]', password) and re.search('[^A-Za-z0-9]', password)):
            raise ValidationError("密码必须包含大写字母、小写字母、数字和特殊字符。")
        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = self.data.get("confirm_password")  # 使用 self.data.get 从请求中获取 confirm_password

        if password and confirm_password and password != confirm_password:
            raise ValidationError("两次输入的密码不一致。")
        return cleaned_data
>>>>>>> 83f1edfc5ffa8e9f876eb602fbd78e4443d636dc
