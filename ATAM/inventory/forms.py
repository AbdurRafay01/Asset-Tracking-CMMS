from django import forms
from tracking.models import Asset,Tracker

class AddAssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields= '__all__'


class AddTrackerForm(forms.ModelForm):
    class Meta:
        model = Tracker
        fields= '__all__'