from Post.views import *
from django.urls import path

urlpatterns = [
    path('detail/<int:pid>/', post_detail, name='detail'),
]
