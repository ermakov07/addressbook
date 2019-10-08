from django.contrib import admin

from .models import ListPeople
from .models import Category


class ListPeopleAdmin(admin.ModelAdmin):
    list_display = ('fam', 'name', 'ot', 'addr', 'birthday', 'note', 'category')
    list_display_links = ('fam',)
#    search_fields = ('fam', 'name')


admin.site.register(ListPeople, ListPeopleAdmin)
admin.site.register(Category)
