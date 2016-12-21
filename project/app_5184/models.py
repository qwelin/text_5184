from django.db import models

class User (models.Model):
    zkid = models.CharField(max_length=12)
    name = models.CharField(max_length=8)
    def __str__(self):
        return self.name

class Text(models.Model):
    zx_id = models.CharField(max_length=12)
    zk_name = models.CharField(max_length=8)
    dat = models.CharField(max_length=6)
    scort = models.CharField(max_length=10)
    subject = models.CharField(max_length=20)
    subject_id = models.CharField(max_length=8)