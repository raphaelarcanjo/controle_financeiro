# Generated by Django 3.2.7 on 2021-10-03 15:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=8)),
                ('data', models.DateField(blank=True, default=datetime.date(2021, 10, 3), null=True)),
                ('fonte', models.CharField(max_length=80)),
                ('extra', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Saida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=8)),
                ('data', models.DateField(blank=True, default=datetime.date(2021, 10, 3), null=True)),
                ('fonte', models.CharField(max_length=80)),
                ('superfluo', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
    ]
