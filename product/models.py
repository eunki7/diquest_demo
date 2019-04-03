from django.contrib.auth.models import User
from django.db import models

from product.fields import ThumbnailImageField


class Product(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    image = ThumbnailImageField(upload_to='product/%Y/%m')
    url = models.URLField('url', unique=True)
    upload_date = models.DateTimeField('Upload Date', auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
