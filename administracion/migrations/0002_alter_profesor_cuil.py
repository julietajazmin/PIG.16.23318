# Generated by Django 3.2.18 on 2023-06-20 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administracion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesor',
            name='cuil',
            field=models.CharField(help_text='Cuil (sin guiones)', max_length=11, verbose_name='Cuil'),
        ),
    ]
