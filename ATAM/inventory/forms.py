from dataclasses import fields
from django import forms
from tracking.models import Asset,Tracker,Job

class AddAssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields= '__all__'


class AddTrackerForm(forms.ModelForm):
    class Meta:
        model = Tracker
        fields= '__all__'
class AddJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
