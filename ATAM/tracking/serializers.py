from rest_framework import serializers
from .models import Location

class LocationSerializer(serializers.ModelSerializer):
    asset_name= serializers.PrimaryKeyRelatedField(source = 'tracker.tracker.asset_name',read_only=True)


    class Meta:
        model = Location
        fields = '__all__'#('id','tracker_id','lat','lng','asset_name')
       