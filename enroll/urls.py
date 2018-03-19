from django.urls import path
from . import views


urlpatterns = [
    path('', views.EnrollPartOne, name="enroll"),
    path('part_two', views.EnrollPartTwo, name="enroll_part_two"),
    path('part_three', views.EnrollPartThree, name="enroll_part_three"),
    path('test', views.Test, name="test"),
    path('application_submitted', views.ApplicationSubmitted, name="application_submitted"),
]
