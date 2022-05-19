from rest_framework import serializers
from .models import User

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'phone_number',)

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'phone_number',)
        extra_kwargs = {'password': {'write_only': True},
                        'phone_number': {'required': True,'allow_blank': False},
                        'email': {'required': True,'allow_blank': False}
        }

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user