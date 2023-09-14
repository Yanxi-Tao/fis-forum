from django.shortcuts import render

def index(request):
    return render(request,"template.html",{"todo_list":todos})