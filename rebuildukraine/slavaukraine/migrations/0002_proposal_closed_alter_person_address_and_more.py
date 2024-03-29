# Generated by Django 4.0.4 on 2022-05-15 19:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slavaukraine', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposal',
            name='closed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='person',
            name='address',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Morada'),
        ),
        migrations.AlterField(
            model_name='person',
            name='birth',
            field=models.DateField(blank=True, null=True, verbose_name='Data de nascimento'),
        ),
        migrations.AlterField(
            model_name='person',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Binary', 'Binary'), ('Nonbinary', 'Nonbinary'), ('Other', 'Other')], max_length=10, null=True, verbose_name='Género'),
        ),
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Último nome'),
        ),
        migrations.AlterField(
            model_name='person',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Imagem de perfil'),
        ),
        migrations.AlterField(
            model_name='person',
            name='taxnumber',
            field=models.CharField(max_length=10, unique=True, validators=[django.core.validators.RegexValidator('^\\d{1,10}$')], verbose_name='Número de Contribuinte'),
        ),
    ]
