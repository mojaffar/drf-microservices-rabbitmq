from django.db import models

# Create your models here.
class Order(models.Model):
    product_name = models.CharField(max_length=255)
    user_email = models.EmailField()
    
