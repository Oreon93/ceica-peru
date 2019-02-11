# Generated by Django 2.0.2 on 2019-01-29 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0038_auto_20190128_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseapplication',
            name='current_spanish_level',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='enroll.AbilityLevel'),
        ),
        migrations.AlterField(
            model_name='courseapplication',
            name='group_number',
            field=models.PositiveSmallIntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4 or more')], default=1, max_length=10),
        ),
    ]