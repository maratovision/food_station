# Generated by Django 3.1.6 on 2021-02-18 11:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cafe', '0007_auto_20210218_1605'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='team',
            options={},
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField(blank=True, max_length=20)),
                ('birth_date', models.DateField(blank=True)),
                ('gender', models.CharField(choices=[('Муж', 'Муж'), ('Жен', 'Жен')], max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
