from .models import Student
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here
def student_list(request):
    student_list = Student.objects.all()
    context = {'student_list': student_list}
    return render(request, 'student/student_list.html', context)

def detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    context = {'student': student}
    return render(request,'student/student_detail.html', context)

