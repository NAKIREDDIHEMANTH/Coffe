# Generated by Django 4.2.6 on 2024-08-28 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=10)),
                ('LastName', models.CharField(max_length=10)),
                ('UserName', models.CharField(max_length=10, unique=True)),
                ('Password', models.CharField(max_length=18)),
                ('RePassword', models.CharField(max_length=18)),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
    ]
