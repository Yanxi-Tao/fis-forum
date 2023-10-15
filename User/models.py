from django.db import models

class users (models.Model):
    Username = models.CharField(max_length=30)
    Email = models.EmailField()
    Gradelevel = models.IntegerField(default=9)

    def __str__(self):
        return self.Username