# Generated by Django 3.2.13 on 2022-06-24 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0006_alter_studentregistration_total_intial_deposit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentregistration',
            old_name='total_intial_deposit',
            new_name='total_initial_deposit',
        ),
    ]
