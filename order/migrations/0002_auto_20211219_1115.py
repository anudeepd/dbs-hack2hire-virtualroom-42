# Generated by Django 3.1.5 on 2021-12-19 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='temp',
            new_name='price',
        ),
    ]