# Generated by Django 3.2.9 on 2021-12-17 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20211216_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='signature',
            field=models.BinaryField(null=True),
        ),
    ]