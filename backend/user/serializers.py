from rest_framework import serializers
from .models import NewUser

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=6, write_only=True)

    class Meta:
        model = NewUser
        fields = ['user_name', 'email', 'password']

    def create(self, validated_data):
        return NewUser.objects.create_user(**validated_data)
