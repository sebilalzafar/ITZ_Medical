from django.db import models
# Create your models here.


available = (
        ('In Stock', 'In Stock'),
        ('Not In Stock', 'Not In Stock'),
    )

class Medicine(models.Model):
    image=models.ImageField( upload_to="images/products/all_medicine", height_field=None, width_field=None, max_length=None,)
    title=models.CharField(max_length=50,)
    description=models.CharField(max_length=50,)
    new_price=models.IntegerField()
    old_price=models.IntegerField()
    availibility=models.CharField(max_length=20,choices = available,)
    
    def __str__(self):
        return self.title
    
