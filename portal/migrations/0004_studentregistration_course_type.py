# Generated by Django 3.2.13 on 2022-06-23 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_studentregistration_driving_license_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentregistration',
            name='course_type',
            field=models.IntegerField(choices=[(1, 'Auto'), (2, 'Manual')], default=1),
            preserve_default=False,
        ),
    ]
