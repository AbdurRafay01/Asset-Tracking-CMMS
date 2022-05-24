from django import forms
from maintenance.models import Maintenance

class AddMaintenanceForm(forms.ModelForm):
    class Meta:
        model = Maintenance
        fields = ['maintenance_limit']

class UpdateMaintenanceForm(forms.ModelForm):
    class Meta:
        model = Maintenance
        fields = ['maintenance_status']