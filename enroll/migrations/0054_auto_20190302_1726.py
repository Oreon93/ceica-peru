# Generated by Django 2.0.2 on 2019-03-02 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0053_auto_20190302_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteerprogram',
            name='accommodation_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='volunteerprogram',
            name='accommodation_es',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='volunteerprogram',
            name='name_en',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='volunteerprogram',
            name='name_es',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='volunteerprogram',
            name='orientation_en',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='volunteerprogram',
            name='orientation_es',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='volunteerprogram',
            name='program_type_en',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='volunteerprogram',
            name='program_type_es',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='volunteerprogram',
            name='spanish_lessons_en',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='volunteerprogram',
            name='spanish_lessons_es',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='volunteerprogram',
            name='volunteer_work_en',
            field=models.CharField(blank=True, default='None', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='volunteerprogram',
            name='volunteer_work_es',
            field=models.CharField(blank=True, default='None', max_length=50, null=True),
        ),
    ]