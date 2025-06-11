import os
from io import BytesIO

from PIL import Image
from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from django.db import models


# Custom function to generate permissions
def custom_permissions(model_name: str):
    permissions = [(f'can_create_{model_name}', f'Can create {model_name}'),
                   (f'can_edit_{model_name}', f'Can edit {model_name}'),
                   (f'can_delete_{model_name}', f'Can delete {model_name}'), ]
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


class CustomModel(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/%Y/%m/%d/', null=True, blank=True)
    thumbnail = models.ImageField(upload_to='thumbnails/%Y/%m/%d/', null=True, blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.pk:
            original = type(self).objects.get(pk=self.pk)
            image_changed = self.image != original.image
        else:
            image_changed = bool(self.image)

        if image_changed:
            if self.image:
                original_io, new_name = reformat_image(self.image)
                self.image.save(new_name, ContentFile(original_io.getvalue()), save=False)

            if not self.thumbnail:
                original_io, new_name = generate_thumbnail(self.image)
                self.thumbnail.save(new_name, ContentFile(original_io.getvalue()), save=False)

        super().save(*args, **kwargs)

    def reformat_image(self):
        original_io, new_name = reformat_image(self.image)
        self.image.save(new_name, ContentFile(original_io.getvalue()), save=False)
        self.save(update_fields=['image'])

    def generate_thumbnail(self):
        original_io, new_name = generate_thumbnail(self.image)
        self.thumbnail.save(new_name, ContentFile(original_io.getvalue()), save=False)
        self.save(update_fields=['thumbnail'])


class Category(CustomModel):
    parent = models.ForeignKey('self', null=True, blank=True, related_name='subcategories', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='category', on_delete=models.PROTECT, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'
        permissions = custom_permissions('category')

    def __str__(self):
        return f'{self.name} - {self.created_by} - {self.created_at}'


class Item(CustomModel):
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


def reformat_image(image):
    image.open()
    img = Image.open(image)
    img = img.convert('RGB')
    original_io = BytesIO()
    original_name = os.path.basename(image.name)
    img.save(original_io, format='WEBP', quality=80)
    new_name = f"{original_name.rsplit('.', 1)[0]}.webp"

    return original_io, new_name


def generate_thumbnail(image):
    image.open()
    img = Image.open(image)
    img = img.convert('RGB')
    img.thumbnail((600, 500))
    original_name = os.path.basename(image.name)
    original_io = BytesIO()
    img.save(original_io, format='WEBP', quality=100)
    new_name = f"thumb_{original_name.rsplit('.', 1)[0]}.webp"

    return original_io, new_name
