# Generated by Django 4.2.2 on 2023-07-31 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_country_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(max_length=80, unique=True),
        ),
    ]
