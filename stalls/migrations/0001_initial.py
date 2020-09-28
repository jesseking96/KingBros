# Generated by Django 3.1 on 2020-09-02 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('floor_type', models.CharField(choices=[('Gravel', 'Gravel'), ('Concrete', 'Concrete')], max_length=256)),
                ('door_height', models.DecimalField(decimal_places=3, max_digits=5)),
                ('width', models.DecimalField(decimal_places=3, max_digits=5)),
                ('length', models.DecimalField(decimal_places=3, max_digits=5)),
                ('number_of_units', models.PositiveIntegerField()),
                ('quarterly_rate', models.DecimalField(decimal_places=2, max_digits=6)),
                ('pic', models.ImageField(blank=True, default='images/default_unit.jpg', upload_to='stall_pics/')),
            ],
        ),
    ]
