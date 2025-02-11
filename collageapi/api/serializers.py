from rest_framework import serializers
from .models import Collage, Student, Faculty

# Create Collage serializers
class CollageSerializers(serializers.HyperlinkedModelSerializer):
    collage_id = serializers.ReadOnlyField()
    class Meta:
        model = Collage
        fields ="__all__"

# Create Student serializers
class StudentSerializers(serializers.HyperlinkedModelSerializer):
    student_id = serializers.ReadOnlyField()
    class Meta:
        model = Student
        fields = "__all__"

# Create Faculty serializers
class FacultySerializers(serializers.HyperlinkedModelSerializer):
    faculty_id = serializers.ReadOnlyField
    class Meta:
        model = Faculty
        fields = "__all__"
