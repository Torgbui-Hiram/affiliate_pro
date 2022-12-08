from django.db import models


class User(models.Model):
    first_name = models.CharField('first_name', max_length=50)
    last_name = models.CharField('last_name', max_length=50)
    password = models.CharField('password', max_length=50)
    password1 = models.CharField('password1', max_length=50)

    def __str__(self):
        return self.first_name + " " + self.last_name
