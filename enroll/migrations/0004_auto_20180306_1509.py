# Generated by Django 2.0.2 on 2018-03-06 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0003_auto_20180306_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='service_description',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
