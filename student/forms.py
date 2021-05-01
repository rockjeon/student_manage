from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Student, Course
# from student.models import Student

class UserForm(UserCreationForm):
    email = forms.EmailField(label='이메일')

# 장고 모델 폼은 내부 class meta 클래스를 반드시 가져와야 하며, meta 에는 모델 폼이 사용할 모델과
# 모델의 필드들을 적어야한다. 즉, model은 User 와 연결 되어 있고, 필드는 username과 email을 사용한다.
    
    class Meta:
        model = User
        fields = ('username', 'email')

class StudentForm(forms.ModelForm):
    model = Student
    class Meta:
        fileds =[
            'name',
            'gender',
            'birth',
            'school',
            'grade',
            'phone',
            'level',
            'create_date',
            'end_date'
        ]

class CourseForm(forms.ModelForm):
    model = Course

    class Meta:
        fields = [
            'main',
            'library',
            'voca_library',
            'count',
            'content',
        ]

