# Generated by Django 5.0.6 on 2024-05-23 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_rename_urls_urldb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urldb',
            name='shortened',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='urldb',
            name='url',
            field=models.CharField(max_length=1000),
        ),
    ]
