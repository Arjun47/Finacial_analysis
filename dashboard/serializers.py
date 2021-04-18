from rest_framework import serializers
from .models import Transaction

class TranSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        # fields = ['id', 'description', 'amount', 'category', 'trans_type', 'created_at']
        fields = '__all__'

