from django.shortcuts import render
from rest_framework import viewsets
from .models import Collage, Student, Faculty
from .serializers import CollageSerializers, StudentSerializers, FacultySerializers
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.

# This is collage views
class CollageViewSet(viewsets.ModelViewSet):
    queryset = Collage.objects.all()
    serializer_class = CollageSerializers

    # Get all faculty and student from collage 
    # collage/{collageId}/student
    # collage/{collageId}/faculty

    @action(detail=True, methods=['get'])
    def student (self, request,pk=None):
        try:
            collage = Collage.objects.get(pk=pk)
            students = Student.objects.filter(collage=collage)
            student_serializer = StudentSerializers(students,many = True, context = {'request':request})
            return Response(student_serializer)
        except Exception as e:
            print(e)
            return Response({
                'message':'Collage may not exist'
            })
    
    @action(detail=True, methods=['gat'])
    def student(self, request, pk=None):
        try:
            collage = Collage.objects.get(pk=pk)
            faculty = Faculty.objects.filter(collage = collage)
            faculty_serializer = FacultySerializers(faculty, manay =True, context = {'request':request})
            return Response(faculty_serializer)
        except Exception as e:
            print(e)
            return Response({
                'message': 'Collage may not exist'
            })


# This is student views
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers


# This is flaculty views
class FacultyViewSet(viewsets.ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializers