from django.contrib import admin
from django.urls import path
from .views import CollageViewSet, StudentViewSet, FacultyViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'collage', CollageViewSet)
router.register(r'student',StudentViewSet)
router.register(r'faculty',FacultyViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
]
