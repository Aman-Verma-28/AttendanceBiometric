from django.db import models
import uuid
import barcode
from barcode.writer import ImageWriter


# Create your models here.
class UserRegistraion(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    role = models.CharField(max_length=100)

    barcode = models.ImageField(upload_to="user_images/", blank=True, null=True)
    token = models.CharField(max_length=100, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + " -> " + self.role

    def save(self, *args, **kwargs):
        self.token = uuid.uuid4().hex[:6].upper()
        self.barcode = self.generate_barcode(self.token)
        super(UserRegistraion, self).save(*args, **kwargs)

    def generate_barcode(self, data, barcode_type="code128"):
        """Generate a barcode for the given data."""
        BARCODE = barcode.get_barcode_class(barcode_type)
        barcode_instance = BARCODE(data, writer=ImageWriter())
        filename = barcode_instance.save(data)
        return filename


class UserAttendance(models.Model):
    user = models.ForeignKey(UserRegistraion, on_delete=models.CASCADE)
    entry = models.DateTimeField(auto_now_add=True)
    exit = models.DateTimeField(null=True, blank=True)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.name + " -> " + str(self.is_present)
