# Generated by Django 2.0.2 on 2018-03-06 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0014_auto_20180306_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='applicant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='enroll.Customer'),
        ),
    ]
