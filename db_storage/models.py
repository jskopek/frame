from django.db import models

# Create your models here.
class Image(models.Model):
    file_name = models.CharField(max_length=255, primary_key=True, unique=True)
    mimetype = models.CharField(max_length=255)
    data = models.BinaryField()
