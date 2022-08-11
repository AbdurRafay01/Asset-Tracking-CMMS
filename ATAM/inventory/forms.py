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
<<<<<<< HEAD
=======
class AddJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = '__all__'
>>>>>>> bd6d0e69e8d3e039c7e3007841949f112760e2e6
