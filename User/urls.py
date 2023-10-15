from User.views import *
from django.urls import path

urlpatterns = [
    path('detail/<int:uid>/', user_detail, name='detail'),
]