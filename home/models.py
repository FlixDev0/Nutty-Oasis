from django.db import models

# Create your models here.
class NutType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    descrption = models.TextField()

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Nut(models.Model):
    name = models.CharField(max_length=100)
    nut_type = models.ForeignKey(NutType,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, default=1)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='nuts_images', blank=True, null=True)
    def __str__(self):
        return self.name
    
        