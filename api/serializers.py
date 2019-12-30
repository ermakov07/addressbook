from rest_framework import serializers
from people.models import Category, ListPeople


class RubricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)

class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListPeople
        fields = ('fam', 'name', 'ot', 'addr', 'birthday', 'note', 'category')