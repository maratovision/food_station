# Generated by Django 3.1.6 on 2021-02-26 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0021_auto_20210226_1939'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.PositiveIntegerField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]