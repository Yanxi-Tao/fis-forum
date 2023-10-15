from Post.views import *
from django.urls import path

urlpatterns = [
    path('index/', post_index, name='index'),
    path('detail/<int:pid>/', post_detail, name='detail'),
]
