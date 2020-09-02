from django.forms import ModelForm
from django import forms

from .models import *

class AddVehicle(ModelForm):
    class Meta:
        model=Vehicle
        fields='__all__'
        exclude=['parkingNumber','outTime','remark','status']