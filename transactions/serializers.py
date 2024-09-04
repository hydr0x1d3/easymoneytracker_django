from rest_framework import serializers
from .models import Transaction, Category


class TransactionSerializer(serializers.ModelSerializer):
    category = serializers.CharField(required=False, allow_null=True)
    date = serializers.DateTimeField(required=False, allow_null=True)

    class Meta:
        model = Transaction
        fields = ['id', 'amount', 'category', 'date']

    def validate_category(self, value):
        if value:
            category, created = Category.objects.get_or_create(name=value)
            return category
        return None
