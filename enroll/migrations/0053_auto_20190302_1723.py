# Generated by Django 2.0.2 on 2019-03-02 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0052_auto_20190302_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteerprogram',
            name='program_type',
            field=models.CharField(max_length=30),
        ),
    ]
