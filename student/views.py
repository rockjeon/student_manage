from .models import Student, Course
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import UserForm
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
    student_list = Student.objects.order_by('-create_date')
    paginator = Paginator(student_list, 10)
    page_obj = paginator.get_page(page)
    context = {'student_list': page_obj}
    return render(request, 'student/student_list.html', context)


@login_required
def detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    context = {'student': student}
    return render(request,'student/student_detail.html', context)

