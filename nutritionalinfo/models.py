from django.db import models

class NutritionalInfo(models.Model):
    '''Model holding nutritional info: 
    - Name: it holds the nutrional value's name
    - Unit: it holds the unit for the nutritional value'''


    name = models.CharField(max_length=50, blank=False, null=False, unique=True)
    unit = models.CharField(max_length=5, blank=False, null=False)

    def __str__(self):
        return "%s (%s)" % (self.name, self.unit)

    class Meta:
        ordering = ['name']
        unique_together = [['name', 'unit']]