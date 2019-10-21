from django.db import models


class ListPeople(models.Model):
    fam = models.CharField(max_length=50, verbose_name='Фамилия')
    name = models.CharField(max_length=50, verbose_name='Имя')
    ot = models.CharField(max_length=50, verbose_name='Отчество')
    addr = models.CharField(max_length=100, verbose_name='Адрес')
    birthday = models.DateField(null=True, blank=True, verbose_name='День рождения')
    note = models.TextField(null=True, blank=True, verbose_name='Заметки')
    category = models.ForeignKey('Category', null=True, on_delete=models.PROTECT, verbose_name='категория')

    class Meta:
        verbose_name_plural = 'Адресная книга'
        verbose_name = 'Запись адресной книги'
        ordering = ['fam']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='категория')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/people/%s/' % self.pk

    class Meta:
        verbose_name_plural = 'Категории'
        verbose_name = 'категорию'
        ordering = ['name']
