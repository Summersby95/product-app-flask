# Generated by Django 3.2.9 on 2021-12-09 10:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ancillaries', '0003_defect'),
        ('products', '0008_operationsmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinishedProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('declared_weight_volume', models.CharField(max_length=20)),
                ('tare_weight', models.CharField(max_length=20)),
                ('minimum_weight_volume', models.CharField(max_length=20)),
                ('target_weight_volume', models.CharField(max_length=20)),
                ('maximum_weight_volume', models.CharField(max_length=20)),
                ('e_mark', models.BooleanField()),
                ('average_weight', models.CharField(max_length=20)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('product', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='DefectSpecification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amber', models.DecimalField(decimal_places=2, max_digits=4)),
                ('red', models.DecimalField(decimal_places=2, max_digits=4)),
                ('comment', models.CharField(max_length=30)),
                ('defect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ancillaries.defect')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]
