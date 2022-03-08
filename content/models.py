from django.db import models
from keywords.models import Keyword

# Create your models here.
class Content(models.Model):
    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    img_url = models.CharField(max_length=255)
    article = models.TextField()

    def __str__(self):
        return self.title