from django.db import models

# Create your models here.
class Keyword(models.Model):
    keyword = models.CharField(max_length=255)
    def __str__(self):
        return self.keyword