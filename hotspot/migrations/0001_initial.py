# Generated by Django 5.0.1 on 2024-01-08 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='hotspot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=15)),
                ('no_telp', models.CharField(max_length=15)),
                ('nama', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]