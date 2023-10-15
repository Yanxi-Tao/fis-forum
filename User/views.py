import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from User.models import users



def user_detail(request,uid):
    user = users.objects.get(pk=uid)
    return render(request,'User/User_detail.html',{'user':user})

def start(request):
    userid = request.session.get('userid',0)

    user = users.objects.filter(id=userid).first()

    return render(request,'login/start.html',{'user':user})

def login(request):
    if request.method == 'GET':
        return render(request,'login/login.html')
    elif request.method == 'POST':
        # 1. data from frontend
        uname = request.POST.get('uname')
        psword = request.POST.get('psword')

        # 2. check if this user is in the database

        user = users.objects.filter(Username=uname,password=psword)
        if user.exists():
            # 3. obtain the user that is currently loging in
            visit = user.first()

            response = redirect(reverse('index'))
            request.session['userid'] = visit.id
            request.session.set_expiry(7*24*3600)
        # 5. redirect
        return response


def register(request):
    if request.method == 'GET':
        return render(request,'login/register.html')
    elif request.method == 'POST':
        #pulling values from frontend
        uname = request.POST.get('uname')
        psword = request.POST.get('psword')
        mail = request.POST.get('mail')
        grade = request.POST.get('grade')

        #determine if the username if already used
        names = users.objects.filter(Username=uname)
        if names.exists():
            return HttpResponse('name already occupied')
        try:
            user = users()
            user.Username = uname
            user.password = psword
            user.Email = mail
            user.Gradelevel = grade
            user.save()
        except:
            return HttpResponse('register failed')

        # redirect after successfully logged in
        return redirect(reverse('user:login'))


def logout(request):
    session_key = request.session.session_key
    request.session.delete(session_key)

    return redirect(reverse('user:start'))