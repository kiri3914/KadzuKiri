from rest_framework import serializers
from .models import User


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['password', 'first_name', 'last_name', 'email', 'phone_number', 'birth_date']
        