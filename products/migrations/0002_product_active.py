# Generated by Django 2.2.17 on 2020-11-17 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='active',
            field=models.TextField(default='yeah, cool'),
        ),
    ]
