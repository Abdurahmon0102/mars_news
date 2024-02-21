from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class New(models.Model):
    news_title = models.CharField(max_length=60)
    desc = models.TextField(max_length=60)
    tags = models.TextField(max_length=60)
    cr = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return
    
class UserProfile(models.Model):
    New = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.New.username
    

