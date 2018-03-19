# Generated by Django 2.0.2 on 2018-03-16 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0034_auto_20180316_1647'),
    ]

    operations = [
        migrations.CreateModel(
            name='VolunteerProgram',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('orientation', models.CharField(max_length=50)),
                ('spanish_lessons', models.CharField(blank=True, max_length=50, null=True)),
                ('accommodation', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
            ],
        ),
    ]
