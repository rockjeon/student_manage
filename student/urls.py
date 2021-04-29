from django.urls import path

from . import views

app_name = 'student'

urlpatterns = [
    path('', views.student_list, name='list'),
    path('<int:student_id>/', views.detail, name='detail'),
]
