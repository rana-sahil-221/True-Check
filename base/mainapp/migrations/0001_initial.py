# Generated by Django 4.1.2 on 2022-11-07 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('msg', models.TextField(max_length=255)),
                ('date', models.DateField()),
            ],
        ),
    ]
