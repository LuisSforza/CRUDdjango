from django.db import models

# Create your models here.
class usuario(models.Model):
    user = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=50)
    def __str__(self): #Para poder ver en texto en el admin y no  como objeto 1
        return self.user
