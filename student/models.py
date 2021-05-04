from django.db import models
# from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator


class Student(models.Model):
    GENDER_CHIOCES = (
        ('M','Male'),
        ('F','Female'),
    )
    MAINCHOICE=(
        ("Library","Library"),
        ("Voca","Voca"),
        ("NF","Library")
    )
    LIBRARYCHOICE = (
        ('R(1:20)','R(1:20)'),
        ('S(1:40)','S(1:40)'),
        ('I(2:00)','I(2:00)')
    )

    VOCALIBRARYCHOICE = (
        ('RV(1:40)','RV(1:40)'),
        ('SV(2:00)','SV(2:00)'),
        ('IV(2:20)','I(2:20)')
    )
    COUNTCHOICE = (
        ('12','12'),
        ('24','24'),
        ('36','36'),
        ('48','48')
    )
    
    # general information
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
    modify_date = models.DateField(null=True, blank=True)
    #  course 
    main = models.CharField(max_length=30, choices=MAINCHOICE, null=True, blank=True)
    library = models.CharField(max_length=30, choices=LIBRARYCHOICE,null=True, blank=True)
    voca_library = models.CharField(max_length=30, choices= VOCALIBRARYCHOICE,null=True, blank=True)
    count = models.CharField(max_length=30, choices= COUNTCHOICE,null=True, blank=True)
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
        



        
# class Course(models.Model):
#     MAINCHOICE=(
#         ("Library","Library"),
#         ("Voca","Voca"),
#         ("NF","Library")
#     )
#     LIBRARYCHOICE = (
#         ('R(1:20)','R(1:20)'),
#         ('S(1:40)','S(1:40)'),
#         ('I(2:00)','I(2:00)')
#     )

#     VOCALIBRARYCHOICE = (
#         ('RV(1:40)','RV(1:40)'),
#         ('SV(2:00)','SV(2:00)'),
#         ('IV(2:20)','I(2:20)')
#     )
#     COUNTCHOICE = (
#         ('12','12'),
#         ('24','24'),
#         ('36','36'),
#         ('48','48')
#     )
#     objects = models.Manager()
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     main = models.CharField(max_length=30, choices=MAINCHOICE)
#     library = models.CharField(max_length=30, choices=LIBRARYCHOICE)
#     voca_library = models.CharField(max_length=30, choices= VOCALIBRARYCHOICE)
#     count = models.CharField(max_length=30, choices= COUNTCHOICE)
#     content = models.TextField()

#     def __str__(self):
#         return str(self.student)