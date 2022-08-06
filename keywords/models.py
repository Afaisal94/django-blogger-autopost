from django.db import models

# Create your models here.
class Keyword(models.Model):
    keyword = models.CharField(max_length=255)
    def __str__(self):
        return self.keyword

class KeywordGroup(models.Model):
    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE)
    keyword_group = models.CharField(max_length=255)
    spintax = models.TextField()
    def __str__(self):
        return self.keyword_group