# Generated by Django 3.1.6 on 2021-02-18 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0012_auto_20210218_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='rating',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
