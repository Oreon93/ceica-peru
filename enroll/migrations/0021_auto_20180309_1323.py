# Generated by Django 2.0.2 on 2018-03-09 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0020_auto_20180309_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=models.TextField(max_length=1000),
        ),
    ]
