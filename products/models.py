from django.db import models
from nutritionalinfo.models import NutritionalInfo

class Products(models.Model):
    '''Model holding products: 
    - Name: it holds the product's name
    - Description: it holds the description of the product
    - Active: It holds active/inactive state'''

    CHOICES = (
        ('ACTIVE', 'Active'),
        ('INACTIVE', 'Inactive'),
    )

    name = models.CharField(max_length=50, blank=False, null=False, unique=True)
    description = models.TextField(blank=False, null=False)
    active = models.CharField(max_length=9,choices=CHOICES,null=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name',]

class NutritionalValues(models.Model):
    '''It holds the nutritional values for each product'''

    product = models.ForeignKey(to=Products, on_delete=models.CASCADE)
    nutritionalinfo = models.ForeignKey(verbose_name="Nutritional information", to=NutritionalInfo, on_delete=models.CASCADE, related_name='nutrivalues')
    value = models.FloatField(blank=False, null=False)

    def __str__(self):
        return "%s: %s" % (str(self.nutritionalinfo), str(self.value))

    class Meta:
        ordering = ['product', 'nutritionalinfo']
        unique_together = [['product', 'nutritionalinfo']]
    