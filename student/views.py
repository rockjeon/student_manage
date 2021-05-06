from .models import Student
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import UserForm, StudentForm
from django.utils import timezone        
# from django.views.generic import ListView

# Create your views here
def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserForm()
    return render(request, 'signup.html', {'form':form})
            
@login_required
def student_list(request):
    
    page = request.GET.get('page', 1)
    student_list = Student.objects.order_by('-id')
    paginator = Paginator(student_list, 10)
    page_obj = paginator.get_page(page)
    context = {'student_list': page_obj}
    return render(request, 'student/student_list.html', context)


@login_required
def detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    context = {'student': student}  
    return render(request,'student/student_detail.html', context)

@login_required
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            user = request.user
            student.author = user
            student.save()
            return redirect ('/')
    else:
        form = StudentForm()
    
    context={'form':form}
    return render(request, 'student/student_form.html', context)


@login_required
def modify(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save(commit=False)
            student.modify_date = timezone.now()  # 수정일시 저장
            student.author = request.user
            student.save()
            return redirect('student:detail', student_id = student.id)
    else:
        form = StudentForm(instance=student)
    context = {'form':form}
    return render(request, 'student/student_form.html',context)

@login_required
def delete(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    student.delete()
    return redirect('student:list')