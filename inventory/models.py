from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Categories belong to users
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Link to the Category model
    purchase_date = models.DateField()
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    warranty_start_date = models.DateField(auto_now=True)
    warranty_end_date = models.DateField(auto_now=True)
    photo = models.ImageField(upload_to='inventory_photos/', null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.user.username})"

    def save(self, *args, **kwargs):
        if not self.warranty_start_date:
            self.warranty_start_date = self.purchase_date
        super().save(*args, **kwargs)
