# Generated by Django 3.2.8 on 2021-10-14 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('candidates', '0003_availablecountry'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appliedjobs',
            options={'verbose_name': 'Applied Jobs', 'verbose_name_plural': 'Applied Jobs'},
        ),
        migrations.AlterModelOptions(
            name='availablecountry',
            options={'verbose_name': 'Available Country', 'verbose_name_plural': 'Available Countries'},
        ),
        migrations.AlterModelOptions(
            name='savedjobs',
            options={'verbose_name': 'Saved Jobs', 'verbose_name_plural': 'Saved Jobs'},
        ),
    ]
