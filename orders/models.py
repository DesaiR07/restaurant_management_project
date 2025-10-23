from django.db import models

# Create your models here.
class orderStatus(models.Model):
    name = models.Charfield(max_length=100, unique=True)

    def __str__(self):
        return self.name



#Updated
class order(models.Model):
    #Existing fields....
    status = models.Foreignkey(
        OrderStatus,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )        