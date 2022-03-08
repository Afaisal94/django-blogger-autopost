from django.db import models

from mail.models import Mail
from blog.models import Blog
from keywords.models import Keyword

# Create your models here.
class Campaign(models.Model):
    STATUS = (
        ('ACTIVE', 'ACTIVE'),
        ('INACTIVE', 'INACTIVE'),
    )
    email = models.ForeignKey(Mail, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE)
    campaign_name = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=STATUS)

    def __str__(self):
        return self.campaign_name