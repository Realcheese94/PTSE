from django.db import models


class SUser(models.Model):
    SuserId = models.CharField(max_length=10,null=False)
    Suserpw = models.CharField(max_length=10,null=False)
    Susername = models.CharField(max_length=5,null=False)
    Susertel = models.CharField(max_length=11,null=False)
    Sinfo = models.TextField(null=True)

    def __str__(self):
        return self.SuserId


# Create your models here.
