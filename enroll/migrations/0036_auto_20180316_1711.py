# Generated by Django 2.0.2 on 2018-03-16 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0035_volunteerprogram'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='service_type',
            field=models.CharField(choices=[('l', 'Lesson'), ('s', 'Special program'), ('e', 'Extra')], default='l', max_length=1),
        ),
    ]
