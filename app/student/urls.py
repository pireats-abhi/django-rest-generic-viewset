from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('student', views.StudentViewsets, basename='students')

app_name = 'student'
urlpatterns = [
    path('', include(router.urls))
]