from django import forms
from .models import *

class input_Form(forms.ModelForm):
    class Meta:
        model = detection_fingures
        fields = ['input_Main_Img']