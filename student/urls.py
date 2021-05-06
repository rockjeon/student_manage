from django.urls import path

from . import views

app_name = 'student'

urlpatterns = [
    path('', views.student_list, name='list'),
    path('detail/<int:student_id>/', views.detail, name='detail'),
    path('modify/<int:student_id>/', views.modify, name='modify'),
    path('delete/<int:student_id>/', views.delete, name='delete'),
    path('create/', views.student_create, name='create'),
]
