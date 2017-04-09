from django.db import models

# Create your models here.
class Sarees (models.Model):
    company = models.CharField(max_length=50)
    price = models.CharField(max_length=10)
    material = models.CharField(max_length=20, null=True)
    category = models.CharField(max_length=50)
    colors = models.CharField(max_length=30, null=True)
    size = models.CharField(max_length=20, null=True)
    details = models.CharField(max_length=90, null=True)
    wash = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.company + " - " + self.price + " \n " +  self.category