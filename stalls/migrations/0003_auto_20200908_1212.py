# Generated by Django 3.1 on 2020-09-08 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stalls', '0002_stall_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stall',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]