from django.db import models

# Create your models here.
class TblBasket(models.Model):
    item = models.CharField(max_length=25, blank=False, null=False)
    quantity = models.IntegerField()
    price = models.IntegerField()
    shopname = models.CharField(max_length=25, blank=False, null=False)

    def __str__(self):
        return self.item

   
