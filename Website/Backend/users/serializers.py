from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['user_name', 'email', 'password', 'musicID', 'musicEmail']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
