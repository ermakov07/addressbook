import datetime
from django.forms import ModelForm
from django.forms import widgets
from django.core.exceptions import ValidationError
import re

from .models import ListPeople
from .models import Category


class PeopleForm(ModelForm):
    """ Form for adding a new entry"""
    class Meta(object):
        model = ListPeople
        fields = ('fam', 'name', 'ot', 'addr', 'birthday', 'note', 'category')
        year = datetime.date.today().year
        widgets = {'birthday': widgets.SelectDateWidget(years=range(year, year-200, -1))}


class CategoryForm(ModelForm):
    """ Form for adding a new category """
    class Meta:
        model = Category
        fields = ('name',)

    def clean(self):
        errors = {}
        if re.search(r'\W', self.cleaned_data['name']) :
            errors['name'] = 'Ошибка, в названии категории должны быть буквы или цифры'
        if errors:
            raise ValidationError(errors)