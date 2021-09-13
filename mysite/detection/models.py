from django.db import models

# Create your models here.
# models.py
class detection_fingures(models.Model):

    input_Main_Img = models.ImageField(upload_to='images/')