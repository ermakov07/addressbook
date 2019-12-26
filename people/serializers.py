from rest_framework import serializers
from .models import Category


class RubricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)
