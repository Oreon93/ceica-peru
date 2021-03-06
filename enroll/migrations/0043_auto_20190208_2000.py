# Generated by Django 2.0.2 on 2019-02-08 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0042_auto_20190208_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='accommodationdescription',
            name='description_en',
            field=models.TextField(max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='accommodationdescription',
            name='description_es',
            field=models.TextField(max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='accommodationdescription',
            name='name_en',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='accommodationdescription',
            name='name_es',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_en',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='faq',
            name='answer_es',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_en',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='faq',
            name='question_es',
            field=models.CharField(max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='volunteerproject',
            name='description_en',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='volunteerproject',
            name='description_es',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='volunteerproject',
            name='project_name_en',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='volunteerproject',
            name='project_name_es',
            field=models.CharField(max_length=45, null=True),
        ),
    ]
