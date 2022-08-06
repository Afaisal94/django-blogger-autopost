from django.db import models
from keywords.models import Keyword

# Create your models here.
class Content(models.Model):
    TYPE = (
        ('NEWS', 'NEWS'),
        ('AGC', 'AGC'),
    )
    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    img_url = models.CharField(max_length=255)
    article = models.TextField()
    type = models.CharField(max_length=10, choices=TYPE)
    permalink = models.CharField(max_length=255)

    def __str__(self):
        return self.title