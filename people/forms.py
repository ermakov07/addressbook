from django.forms import ModelForm

from .models import ListPeople
from .models import Category


class PeopleForm(ModelForm):
    """ Form for adding a new entry"""
    class Meta:
        model = ListPeople
        fields = ('fam', 'name', 'ot', 'addr', 'birthday', 'note', 'category')


class CategoryForm(ModelForm):
    """ Form for adding a new category """
    class Meta:
        model = Category
        fields = ('name',)
