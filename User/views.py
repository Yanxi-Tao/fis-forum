from django.shortcuts import render
from User.models import users

def user_detail(request,uid):
    user = users.objects.get(pk=uid)
    return render(request,'User/User_detail.html',{'user':user})
