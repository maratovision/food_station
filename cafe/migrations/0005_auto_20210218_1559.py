# Generated by Django 3.1.6 on 2021-02-18 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0004_auto_20210218_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='image',
            field=models.ImageField(blank=True, default='team_image.png', upload_to=''),
        ),
    ]
