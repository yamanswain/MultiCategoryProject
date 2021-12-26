from django.db import models

# Create your models here.


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    c_name = models.CharField(max_length=200, blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')

    class Meta:
        unique_together = ('parent', 'c_name')
        verbose_name_plural = "categories"

    def __str__(self):
        return str(self.c_name)


class Product(models.Model):
    p_name = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=8, decimal_places=3)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.p_name
