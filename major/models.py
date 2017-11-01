from django.db import models

class user(models.Model):
    name = models.CharField(max_length=140)
    password =models.CharField(max_length=140)
    def __str__(self):
        return self.name