# Generated by Django 2.2.6 on 2019-10-14 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0003_auto_20191008_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listpeople',
            name='birthday',
            field=models.DateField(blank=True, null=True, verbose_name='День рождения'),
        ),
    ]