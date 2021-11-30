from django import forms
from .models import *

class add_reader(forms.ModelForm):
    class Meta:
        model = reader
        fields = ["RName","RNumber","Gender","City","ContactNumber","Subscription"]
        labels = {
            'RName':'',
            'RNumber':'',
            'Gender':'',
            'City':'',
            'ContactNumber':'',
            'Subscription':'Choose Your Plan'
        }
        widgets={
            'RName':forms.TextInput(attrs={'class':'form-control text-inputs','placeholder':'Enter your Name'}),
            'RNumber':forms.TextInput(attrs={'class':'form-control text-inputs','placeholder':'Enter your unique ID'}),
            'Gender':forms.RadioSelect(choices=GENDER_CHOICES,attrs={'class':''}),
            'City':forms.TextInput(attrs={'class':'form-control text-inputs','placeholder':'Enter your City'}),
            'ContactNumber':forms.TextInput(attrs={'class':'form-control text-inputs','placeholder':'Enter your Mobile No.'}),
            'Subscription':forms.Select(attrs={'class':'form-select text-input'})
        }