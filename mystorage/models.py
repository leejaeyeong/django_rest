from django.db import models
from django.conf import settings

class Essay(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1,on_delete=models.CASCADE) # user에 맞게 정해지도록 설정합니다.
    title = models.CharField(max_length=30)
    body = models.TextField()