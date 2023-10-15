
from django.db import models
from Subject.models import Subject
from User.models import users
from django.utils import timezone

class posts(models.Model):
        author = models.ForeignKey( users , on_delete=models.PROTECT,verbose_name='author')
        title = models.CharField(max_length=200)
        content = models.TextField(max_length=3000)
        subject = models.ForeignKey( Subject ,on_delete=models.PROTECT,verbose_name='subject')
        publish_date = models.DateField(verbose_name='publish date',default=timezone.now())

        def __str__(self):
            return self.title