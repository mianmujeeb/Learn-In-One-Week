# Generated by Django 3.2.13 on 2022-06-23 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0004_studentregistration_course_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentregistration',
            name='registration_id',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentregistration',
            name='total_intial_deposit',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=999),
            preserve_default=False,
        ),
    ]