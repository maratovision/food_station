# Generated by Django 3.1.6 on 2021-02-18 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0011_auto_20210218_1717'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='name',
            new_name='full_name',
        ),
        migrations.AddField(
            model_name='team',
            name='age',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='team',
            name='rating',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
