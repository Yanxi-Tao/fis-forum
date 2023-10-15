from django.shortcuts import render
from Post.models import posts

def post_index(request):
    post = posts.objects.all()
    return render(request,'Post/Post_Index.html',{'posts':post})

def post_detail(request, pid):
    post = posts.objects.get(pk=pid)
    return render(request,'Post/Post_detail.html',{'posts':post})
