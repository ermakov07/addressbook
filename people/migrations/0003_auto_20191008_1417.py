# Generated by Django 2.2.6 on 2019-10-08 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_auto_20191008_1350'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name': 'категорию', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterField(
            model_name='listpeople',
            name='birthday',
            field=models.DateField(null=True),
        ),
    ]
