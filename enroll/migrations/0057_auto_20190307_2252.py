# Generated by Django 2.0.2 on 2019-03-07 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0056_auto_20190307_2251'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='service_type_en',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='service_type_es',
            field=models.CharField(max_length=60, null=True),
        ),
    ]