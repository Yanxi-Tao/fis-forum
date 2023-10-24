from User.views import *
from django.urls import path


urlpatterns = [

    path('start/', start, name='start'),

    path('register/', register, name='register'),

    path('login/', login, name='login'),

    path('logout/', logout, name = 'logout'),

    path('detail/<int:uid>/', user_detail, name='detail'),


]