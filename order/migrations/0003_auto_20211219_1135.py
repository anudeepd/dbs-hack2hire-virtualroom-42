# Generated by Django 3.1.5 on 2021-12-19 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20211219_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='orderstatus',
            field=models.CharField(choices=[('PLACED', 'PLACED'), ('PROCESSED', 'PROCESSED'), ('ACCEPTED', 'ACCEPTED'), ('REJECTED', 'REJECTED')], default=('PLACED', 'PLACED'), max_length=20),
        ),
    ]
