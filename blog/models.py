from django.db import models
from mail.models import Mail

# Create your models here.
class Blog(models.Model):
    email = models.ForeignKey(Mail, on_delete=models.CASCADE)
    blog = models.CharField(max_length=255)
    email_post = models.EmailField(max_length=255, unique=True)
    batch = models.IntegerField()
    url_blogger = models.CharField(max_length=255)

    def __str__(self):
        return self.blog