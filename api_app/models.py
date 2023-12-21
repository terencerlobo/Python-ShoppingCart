from django.db import models

class CartItem(models.Model):
    product_quantity = models.PositiveIntegerField()
    product_name = models.CharField(max_length=200)
    product_price = models.FloatField()