from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

class Student(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=5)
    phone = models.CharField(max_length=20)
    level = models.PositiveIntegerField(default=10, validators=[MinValueValidator(1), MaxValueValidator(10)])
    create_date = models.DateField()

    def __str__(self):
        return self.name