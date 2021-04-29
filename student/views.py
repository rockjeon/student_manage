from .models import Student
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator

# Create your views here
def index(request):
    return render(request, 'index.html')

def signup(request):
    return render(request, 'signup.html')

def student_list(request):
    page = request.GET.get('page', 1)
    student_list = Student.objects.order_by('-create_date')
    paginator = Paginator(student_list, 10)
    page_obj = paginator.get_page(page)
    context = {'student_list': page_obj}
    return render(request, 'student/student_list.html', context)



def detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    context = {'student': student}
    return render(request,'student/student_detail.html', context)

