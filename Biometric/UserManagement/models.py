import os
import uuid

import barcode
from barcode.writer import ImageWriter
from django.conf import settings
from django.db import models


def generate_barcode(data, upload_to, barcode_type="code128"):
    """Generate a barcode image and save it under MEDIA_ROOT/upload_to."""
    output_dir = os.path.join(settings.MEDIA_ROOT, upload_to)
    os.makedirs(output_dir, exist_ok=True)

    barcode_class = barcode.get_barcode_class(barcode_type)
    barcode_instance = barcode_class(data, writer=ImageWriter())
    filepath = barcode_instance.save(os.path.join(output_dir, data))
    # Return path relative to MEDIA_ROOT for the ImageField
    return os.path.relpath(filepath, settings.MEDIA_ROOT)


class UserRegistraion(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    role = models.CharField(max_length=100)

    barcode = models.ImageField(upload_to="user_images/", blank=True, null=True)
    token = models.CharField(max_length=100, blank=True, null=True, unique=True)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + " -> " + self.role

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = uuid.uuid4().hex.upper()
        super().save(*args, **kwargs)
        if not self.barcode:
            self.barcode = generate_barcode(self.token, "user_images")
            super().save(update_fields=["barcode"])


class UserAttendance(models.Model):
    user = models.ForeignKey(UserRegistraion, on_delete=models.CASCADE)
    item = models.ForeignKey("Item", on_delete=models.CASCADE, default=None)
    entry = models.DateTimeField(auto_now_add=True)
    exit = models.DateTimeField(null=True, blank=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.name + " -> " + str(self.is_active)


class Item(models.Model):
    name = models.CharField(max_length=100)
    barcode = models.ImageField(upload_to="item_images/", blank=True, null=True)
    token = models.CharField(max_length=100, blank=True, null=True, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.token:
            self.token = uuid.uuid4().hex.upper()
        super().save(*args, **kwargs)
        if not self.barcode:
            self.barcode = generate_barcode(self.token, "item_images")
            super().save(update_fields=["barcode"])
