from django.db import models
from django.conf import settings

class Post(models.Model):
        author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
        title = models.CharField(max_length=100)
        content = models.TextField()
        is_public = models.BooleanField(default=False)
        ip= models.CharField(max_length=40, blank=True)

        class Meta:
                ordering = ('-id',)

# Create your models here.
