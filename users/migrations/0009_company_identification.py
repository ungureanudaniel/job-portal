# Generated by Django 3.2.8 on 2022-01-12 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_rename_date_candidate_birthdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='identification',
            field=models.CharField(default='a', max_length=20),
            preserve_default=False,
        ),
    ]