"""
URL configuration for fis_forum project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

import Post.views
from Post.views import *
from User.views import start

urlpatterns = [

    path('', start),

    path('api-auth/', include('rest_framework.urls')),

    path('admin/', admin.site.urls),
    #homepage
    path('index/', post_index, name='index'),
    #app pages
    path('user/', include(('User.urls', 'User'), namespace='user')),

    path('post/', include(('Post.urls', 'Post'), namespace='post')),

    path('Subject/', include(('Subject.urls', 'Subject'), namespace='subject')),

    #path('index/', Post.views.LoginView.as_view() ),
]
