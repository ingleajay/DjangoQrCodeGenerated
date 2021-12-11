from django.db import models

# Create your models here.


class UserLink(models.Model):
    username = models.CharField(max_length=70, default='not have username')
    qr_link = models.CharField(max_length=70, default='not have qr_link')
    qr_title = models.CharField(max_length=70, default='not have qr_title')
    # qr_img = models.FileField(null=True)

    def __str__(self):
        return self.username
