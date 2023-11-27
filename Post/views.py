from django.shortcuts import render, redirect, reverse
from Post.models import posts
from User.models import users
from django.http import JsonResponse, HttpResponse
from Subject.models import Subject
from rest_framework.response import Response


def post_index(request):
    if request.method == 'GET':
        post = posts.objects.all()
        userid = request.session.get('userid', 0)
        user = users.objects.filter(id=userid).first()
        return render(request, 'Post/Post_Index.html', {'posts': post, 'user': user})
    elif request.method == 'POST':
        content = request.POST.get('search')
        post = posts.objects.filter(title__icontains = content)
        if post.exists():
            print(post)
            return render(request,'Post/Post_list.html',{'posts':post})
        else:
            return HttpResponse('no post found')



def post_detail(request, pid):
    post = posts.objects.get(pk=pid)
    a = {'title': post.title, 'subject': str(post.subject), 'author': str(post.author), 'content': post.content}
    # return JsonResponse(a,safe = False)
    return render(request, 'Post/Post_detail.html', {'posts': post})

def new_post(request):
    userid = request.session.get('userid', 0)
    if request.method == 'GET':
        subject = Subject.objects.all()

        return render(request,'Post/Post_new.html', {'subject': subject})
    elif request.method == 'POST':
        sid = request.POST.get('subject')
        post = posts()
        post.author_id = userid
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.subject = Subject.objects.get(id = sid)
        post.save()
        return redirect(reverse('index'))

