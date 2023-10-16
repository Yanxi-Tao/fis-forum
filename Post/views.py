from django.shortcuts import render
from Post.models import posts
from User.models import users
from django.http import JsonResponse

def post_index(request):
    post = posts.objects.all()
    userid = request.session.get('userid',0)
    user = users.objects.filter(id=userid).first()
    #return JsonResponse(post,user)
    return render(request,'Post/Post_Index.html',{'posts':post,'user':user})

def post_detail(request, pid):
    post = posts.objects.get(pk=pid)
    a = {'title': post.title, 'subject': str(post.subject), 'author': str(post.author), 'content': post.content}
    return JsonResponse(a,safe = False)
    #return render(request,'Post/Post_detail.html',{'posts':post})


