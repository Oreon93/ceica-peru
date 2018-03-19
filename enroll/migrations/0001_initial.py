# Generated by Django 2.0.2 on 2018-03-06 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email_address', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('whatsapp', models.CharField(max_length=15)),
                ('Nationality', models.CharField(max_length=15)),
                ('passport_number', models.CharField(max_length=12)),
                ('occupation', models.CharField(max_length=30)),
                ('emergency_name', models.CharField(max_length=60)),
                ('emergency_number', models.CharField(max_length=15)),
                ('gender', models.CharField(choices=[('m', 'Male'), ('f', 'Female'), ('o', 'Other'), ('p', 'Prefer not to say')], max_length=1)),
                ('marital_status', models.CharField(choices=[('m', 'Married'), ('s', 'Single')], max_length=1)),
            ],
            options={
                'ordering': ['first_name'],
            },
        ),
    ]
