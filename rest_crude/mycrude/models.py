from django.db import models

# Create your models here.


class Mycrude(models.Model):
    class Meta:
        db_table = 'Mycrude'

    name = models.CharField(max_length = 255 , null = False)
    description = models.CharField(max_length = 255 , null = False)
    published = models.BooleanField(default = False , null = False)
