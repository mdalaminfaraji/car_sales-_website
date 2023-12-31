from django.db import models
from django.contrib.auth.models import User

class Brand(models.Model):
    name = models.CharField(max_length=100)
    slug=models.SlugField(max_length=100, unique=True, null=True,blank=True)
    def __str__(self):
            return self.name

class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='cars/media/uploads' ,blank=True, null=True)
    
    def __str__(self):
            return self.name
    

class Comment(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comments')
    name=models.CharField(max_length=30)
    comment = models.TextField()
    created_on=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Comments by {self.name}"


class Order(models.Model):
        user=models.ForeignKey(User, on_delete=models.CASCADE)
        car=models.ForeignKey(Car, on_delete=models.CASCADE)
        date=models.DateTimeField(auto_now_add=True)



