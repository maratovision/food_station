# Generated by Django 3.1.6 on 2021-03-03 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0029_auto_20210303_1904'),
    ]

    operations = [
        migrations.CreateModel(
            name='RatingStar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.SmallIntegerField(default=0, verbose_name='Значение')),
            ],
        ),
        migrations.RemoveField(
            model_name='rate',
            name='rate',
        ),
    ]
