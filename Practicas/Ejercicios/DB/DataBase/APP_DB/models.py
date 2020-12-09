from django.db import models

# Create your models here.
class ejemplo_1(models.Model):
    campo_ejemplo1 = models.CharField(max_length=100, primary_key=True)
    campo_ejemplo2 = models.CharField(max_length=100)
    campo_ejemplo3 = models.CharField(max_length=100)
    campo_ejemplo4 = models.CharField(max_length=100)

class ejemplo_2(models.Model):
    campo_ejemplo1 = models.ForeignKey(ejemplo_1, on_delete=models.CASCADE)
    campo_ejemplo2 = models.CharField(max_length=100)
    campo_ejemplo3 = models.CharField(max_length=100)
    campo_ejemplo4 = models.CharField(max_length=100)