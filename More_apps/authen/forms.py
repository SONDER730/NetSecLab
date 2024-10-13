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