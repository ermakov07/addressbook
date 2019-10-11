from django.forms import ModelForm

from .models import ListPeople


class PeopleForm(ModelForm):
    class Meta:
        model = ListPeople
        fields = ('fam', 'name', 'ot', 'addr', 'birthday', 'note', 'category')
