from django.db import models
# from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator


class Student(models.Model):
    GENDER_CHIOCES = (
        ('M','Male'),
        ('F','Female'),
    )
    
    objects = models.Manager()
    name = models.CharField(max_length=5)
    gender = models.CharField(max_length=200, choices=GENDER_CHIOCES)
    birth = models.DateField()
    school = models.CharField(max_length=50)
    grade = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(6)])
    phone = models.CharField(max_length=20)
    level = models.PositiveIntegerField(null=True, blank=True)
    create_date = models.DateField()
    end_date = models.DateField()
    
    def __str__(self):
        return self.name


