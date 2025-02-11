from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

#  This is Collage Model
class Collage(models.Model):
    collage_id = models.AutoField(primary_key=True)
    collage_name = models.CharField(max_length=100)
    collage_addgress = models.CharField(max_length=100)
    collage_email = models.CharField(max_length=50)
    collage_type = models.CharField(max_length=50,choices=(
        ('Engineering','Engineering'),
        ('Medical','Medical'),
        ('Arts','Arts'),
        ('Business','Business'),
        ('MBA','MBA')
    )) 
    collage_phone = models.CharField(max_length=10)
    collage_about = models.TextField()
    active = models.BooleanField(default=True)
    timeDate = models.DateTimeField(auto_now=True)

# This is Student model
class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=50)
    student_email = models.EmailField(max_length=50)
    student_phone = PhoneNumberField(max_length=10)
    student_degree = models.CharField(max_length=50, choices=(
        ('Graduation','Graduation'),
        ('Post Graduation', 'Post Graduation'),
        ('PHD','PHD')
    ))
    student_degree_specific = models.CharField(max_length=50,choices=(
        ('BTech','BTech'),
        ('BE','BE'),
        ('MBBS','MBBS'),
        ('MD','MD'),
        ('BCom','BCom'),
        ('BSc','BBc')
    ))
    student_addmission_date = models.DateTimeField(auto_now=True)
    student_about = models.TextField()
    student_collage = models.ForeignKey(Collage, on_delete=models.CASCADE)

# This is Faculty
class Faculty(models.Model):
    faculty_id = models.AutoField(primary_key=True)
    faculty_name = models.CharField(max_length=50)
    faculty_email = models.EmailField(max_length=50)
    faculty_phone = PhoneNumberField(max_length=10)
    faculty_type = models.CharField(max_length=50, choices=(
        ('Cleaning Staff','Cleaning Staff'),
        ('Professor', 'Professor'),
        ('Accountant Staff','Accountant Staff'),
        ('Laboratory Staff','Laboratory Staff')
    ))
    faculty_about = models.TextField()
    faculty_exprience = models.IntegerField()
    faculty_collage = models.ForeignKey(Collage, on_delete=models.CASCADE)

