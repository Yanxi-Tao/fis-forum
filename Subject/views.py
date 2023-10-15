from django.shortcuts import render
from Subject.models import Subject

def subject_detail(request):
    subjects = Subject.objects.all()
    return render(request,'Subject/Subject_detail.html',{'subjects':subjects})