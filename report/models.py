from django.db import models

from blog.models import Blog
from keywords.models import Keyword

# Create your models here.
class Report(models.Model):
    STATUS = (
        ('SUCCESS', 'SUCCESS'),
        ('FAILED', 'FAILED'),
    )
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE)
    postdate = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS)

    def __str__(self):
        return self.postdate