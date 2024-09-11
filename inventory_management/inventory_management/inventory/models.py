from django.db import models

# Create your models here.
class InventoryItem(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    supplier = models.CharField(max_length=100)
    added_date = models.DateField()

    def __str__(self):
        return self.name