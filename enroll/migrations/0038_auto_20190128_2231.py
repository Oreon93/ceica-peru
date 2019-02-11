# Generated by Django 2.0.2 on 2019-01-28 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0037_volunteerprogram_program_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteerprogram',
            name='volunteer_work',
            field=models.CharField(blank=True, default='None', max_length=50),
        ),
        migrations.AlterField(
            model_name='courseapplication',
            name='group_number',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4 or more', '4 or more')], default='1', max_length=1),
        ),
    ]
