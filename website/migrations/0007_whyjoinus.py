# Generated by Django 3.2.13 on 2022-06-21 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_benifit'),
    ]

    operations = [
        migrations.CreateModel(
            name='WhyJoinUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Why Join Us',
                'verbose_name_plural': 'Why Join Us',
            },
        ),
    ]
