# Generated by Django 2.0.2 on 2019-03-07 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0054_auto_20190302_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='description_en',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='feature',
            name='description_es',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='feature',
            name='name_en',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='feature',
            name='name_es',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question',
            field=models.CharField(max_length=160),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question_en',
            field=models.CharField(max_length=160, null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='question_es',
            field=models.CharField(max_length=160, null=True),
        ),
    ]
