from django.db import models


class Phone(models.Model):
    name        = models.CharField(max_length=255)
    description = models.TextField(default='', blank=True)
    url         = models.URLField(unique=True)
    color       = models.CharField(max_length=20)
    ram         = models.IntegerField()
    memory      = models.IntegerField()
    brend       = models.CharField(max_length=20)
    price       = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.name} - {self.brend}'
    