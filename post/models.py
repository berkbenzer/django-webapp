from django.db import models


class yazi (models.Model):
    başlık = models.CharField(max_length=120)
    metin = models.TextField()
