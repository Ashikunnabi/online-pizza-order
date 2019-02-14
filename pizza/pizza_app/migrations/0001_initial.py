# Generated by Django 2.1.5 on 2019-01-22 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('size', models.CharField(choices=[('R', 'Regular'), ('B', 'Big'), ('S', 'Small')], max_length=1)),
                ('current_price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('previous_price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]
