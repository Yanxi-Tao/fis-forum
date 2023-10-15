from django.db import models
from Subject.models import Subject
from User.models import users

class posts(models.Model):
    author = models.ForeignKey( users , on_delete=models.PROTECT,verbose_name='author')
    title = models.CharField(max_length=200)
    context = models.TextField(max_length=3000)
    subject = models.ForeignKey( Subject ,on_delete=models.PROTECT,verbose_name='subject')