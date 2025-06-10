from django.contrib.auth.models import User
from django.db import models


# Custom function to generate permissions
def custom_permissions(model_name: str):
    permissions = [
        (f'can_create_{model_name}', f'Can create {model_name}'),
        (f'can_edit_{model_name}', f'Can edit {model_name}'),
        (f'can_delete_{model_name}', f'Can delete {model_name}'),
    ]
    return permissions


class Currency(models.Model):
    name = models.CharField(max_length=255)
    symbol = models.CharField(max_length=20)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Currencies'
        permissions = custom_permissions('currency')

    def __str__(self):
        return self.name


class Category(models.Model):
    image = models.ImageField(upload_to='category/%Y/%m/%d/', null=True, blank=True)
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='subcategories', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='category', on_delete=models.PROTECT, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'
        permissions = custom_permissions('category')

    def __str__(self):
        return self.name


class Item(models.Model):
    image = models.ImageField(upload_to='item/%Y/%m/%d/', null=True, blank=True)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, null=True, blank=True, related_name='item', on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    currency = models.ForeignKey(Currency, null=True, related_name='item', on_delete=models.SET_NULL)
    detail = models.TextField(blank=True, null=True)
    is_special = models.BooleanField(default=False)
    out_of_stock = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='item', on_delete=models.PROTECT, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)
        permissions = custom_permissions('item')

    def __str__(self):
        return f'{self.name} - {self.created_by} - {self.created_at}'
