# Generated by Django 2.0.2 on 2019-03-10 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0058_auto_20190310_1910'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='question_type_en',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_type_es',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
