from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)

class Food(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name=models.CharField(max_length=20)
    price = models.IntegerField()
    description = models.TextField()
    image_url = models.URLField()