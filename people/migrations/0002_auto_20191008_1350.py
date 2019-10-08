# Generated by Django 2.2.6 on 2019-10-08 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='категория')),
            ],
            options={
                'verbose_name_plural': 'Категория 1',
                'verbose_name': 'Категория 2',
                'ordering': ['name'],
            },
        ),
        migrations.AlterModelOptions(
            name='listpeople',
            options={'ordering': ['fam'], 'verbose_name': 'Запись адресной книги', 'verbose_name_plural': 'Адресная книга'},
        ),
        migrations.AlterField(
            model_name='listpeople',
            name='addr',
            field=models.CharField(max_length=100, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='listpeople',
            name='birthday',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='listpeople',
            name='fam',
            field=models.CharField(max_length=50, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='listpeople',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='listpeople',
            name='note',
            field=models.TextField(blank=True, null=True, verbose_name='Заметки'),
        ),
        migrations.AlterField(
            model_name='listpeople',
            name='ot',
            field=models.CharField(max_length=50, verbose_name='Отчество'),
        ),
        migrations.AddField(
            model_name='listpeople',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='people.Category', verbose_name='категория'),
        ),
    ]
