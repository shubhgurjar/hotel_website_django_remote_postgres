from django.db import models

# Create your models here.
class Customer(models.Model):
    customer_name = models.CharField(max_length=50)
    customer_email = models.EmailField(max_length=100)
    customer_msg = models.CharField(max_length=1000)

    def __str__(self):
        return f"{self.customer_name}"