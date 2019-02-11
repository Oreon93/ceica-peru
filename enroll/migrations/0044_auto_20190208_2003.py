# Generated by Django 2.0.2 on 2019-02-08 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0043_auto_20190208_2000'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='description_en',
            field=models.TextField(help_text='(Or quote)', max_length=800, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='description_es',
            field=models.TextField(help_text='(Or quote)', max_length=800, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='title_en',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='title_es',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
