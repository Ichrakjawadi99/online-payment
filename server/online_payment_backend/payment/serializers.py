# payment/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Payment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['card_number', 'expiry_date', 'cvv', 'amount']
