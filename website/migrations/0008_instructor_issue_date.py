# Generated by Django 3.2.13 on 2022-06-21 21:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_whyjoinus'),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='issue_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
