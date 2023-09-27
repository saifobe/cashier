from rest_framework import serializers
from .models import User, Product, Transaction_items, Transaction

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class PaymentItemSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    qty = serializers.IntegerField()

class PaymentSerializer(serializers.Serializer):
    items = PaymentItemSerializer(many=True)

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'