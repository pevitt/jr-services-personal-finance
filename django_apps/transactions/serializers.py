from rest_framework import serializers
from django_apps.transactions.models import Transaction

class TransactionInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['balance', 'category', 'amount', 'description', 'external_id']

class TransactionOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'balance', 'external_id', 'category', 'amount', 'description', 'created_at', 'updated_at']

class TransactionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['category', 'amount', 'description']
        extra_kwargs = {
            'category': {'required': False},
            'amount': {'required': False},
            'description': {'required': False},
        }