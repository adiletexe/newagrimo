# Generated by Django 4.1.7 on 2023-07-05 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_sunradiation_userprofile_sunradiation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='telephone',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
