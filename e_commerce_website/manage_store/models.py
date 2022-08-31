from django.db import models

class Category(models.Model):
    c_name = models.CharField(max_length=100, unique=True)
    c_description = models.CharField(max_length=1000)
    c_img = models.ImageField(null=True, blank=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.c_name

class Product(models.Model):
    p_name = models.CharField(max_length=200)
    p_code = models.CharField(max_length=50, unique=True)
    p_description = models.CharField(max_length=500)
    p_image = models.ImageField(null=True, blank=True)
    p_stock = models.PositiveIntegerField()
    p_price = models.DecimalField(max_digits=10, decimal_places=2)
    p_uploaded_date = models.DateTimeField(auto_now_add=True)
    p_updated_date = models.DateTimeField(auto_now=True)
    p_category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.p_name
    
