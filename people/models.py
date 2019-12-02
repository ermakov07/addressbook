from django.db import models


class ListPeople(models.Model):
    fam = models.CharField(max_length=50, verbose_name='Surname')
    name = models.CharField(max_length=50, verbose_name='Name')
    ot = models.CharField(max_length=50, verbose_name='Patronymic')
    addr = models.CharField(max_length=100, verbose_name='addr')
    birthday = models.DateField(null=True, blank=True, verbose_name='Birthday')
    note = models.TextField(null=True, blank=True, verbose_name='Note')
    category = models.ForeignKey('Category', null=True, on_delete=models.PROTECT, verbose_name='category')

    class Meta:
        verbose_name_plural = 'Famous People'
        verbose_name = 'Famous People'
        ordering = ['fam']

    def get_absolute_url(self):
        return '/people/people/%s' % self.pk


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='category')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/people/%s/' % self.pk

    class Meta:
        verbose_name_plural = 'categoryes'
        verbose_name = 'category'
        ordering = ['name']
