# Generated by Django 2.0.2 on 2018-03-16 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0032_volunteerproject'),
    ]

    operations = [
        migrations.RenameField(
            model_name='volunteerproject',
            old_name='level_description',
            new_name='description',
        ),
    ]
