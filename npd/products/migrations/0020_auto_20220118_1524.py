# Generated by Django 3.2.9 on 2022-01-18 15:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_auto_20220117_1145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='finishedproduct',
            name='average_weight',
        ),
        migrations.RemoveField(
            model_name='finishedproduct',
            name='maximum_weight_volume',
        ),
        migrations.RemoveField(
            model_name='finishedproduct',
            name='minimum_weight_volume',
        ),
        migrations.RemoveField(
            model_name='finishedproduct',
            name='target_weight_volume',
        ),
        migrations.AddField(
            model_name='commercialmodel',
            name='organic',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='finishedproduct',
            name='packaging_artwork_approved',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='finishedproduct',
            name='tare_weight',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('[g, kg]$', 'Must end with g or kg')]),
        ),
        migrations.AlterField(
            model_name='innerpackaging',
            name='key_line',
            field=models.BooleanField(verbose_name='Key Line Confirmed'),
        ),
        migrations.AlterField(
            model_name='operationsmodel',
            name='test_date',
            field=models.DateField(verbose_name='Production Run Test Date'),
        ),
    ]
