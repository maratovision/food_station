# Generated by Django 3.1.6 on 2021-02-26 13:39

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0020_auto_20210221_2235'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateField(default=datetime.date(2021, 2, 26)),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('house', models.CharField(max_length=10)),
                ('pay_method', models.CharField(choices=[('VISA/Bank account', 'VISA/Bank account'), ('PayPal', 'PayPal'), ('Cash', 'Cash')], max_length=30)),
                ('food', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cafe.food')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cafe.client')),
            ],
        ),
    ]
