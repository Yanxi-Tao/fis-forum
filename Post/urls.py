from Post.views import *
from rest_framework import routers
from django.urls import path


urlpatterns = [

    path('detail/<int:pid>/', post_detail, name='detail'),

]
