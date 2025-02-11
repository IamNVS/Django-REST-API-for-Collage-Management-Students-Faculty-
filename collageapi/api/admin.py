from django.contrib import admin
from .models import Collage,Student,Faculty

# Register your models here.
class CollageAdmin(admin.ModelAdmin):
    list_display = ('collage_id','collage_name','collage_addgress','collage_type')
    search_fields =('collage_name')

class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id','student_name','student_degree','student_degree_specific','student_collage')
    search_fields = ('student_name','student_collage')

class FacultyAdmin(admin.ModelAdmin):
    list_display = ('faculty_id','faculty_name','faculty_collage')
    search_fields = ('faculty_name','faculty_collage')

