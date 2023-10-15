from Subject.views import *
from django.urls import path

urlpatterns = [
    path('detail', subject_detail, name='subject'),
]