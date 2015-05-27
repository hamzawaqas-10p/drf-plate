from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField('First Name', max_length=30)
    middle_name = models.CharField('Middle Name', max_length=30, default='a')
    last_name = models.CharField('Last Name', max_length=30)