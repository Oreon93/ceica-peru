# Generated by Django 2.0.2 on 2018-03-06 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0005_customer_type_price'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Customer_type',
            new_name='CustomerType',
        ),
    ]

    atomic = False
