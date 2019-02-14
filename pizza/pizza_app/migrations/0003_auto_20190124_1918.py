# Generated by Django 2.1.5 on 2019-01-24 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_app', '0002_auto_20190122_1816'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pizza',
            old_name='current_price',
            new_name='current_big_pizzaprice',
        ),
        migrations.RenameField(
            model_name='pizza',
            old_name='previous_price',
            new_name='previous_regular_pizza_price',
        ),
        migrations.AddField(
            model_name='pizza',
            name='current_regular_pizzaprice',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pizza',
            name='current_small_pizzaprice',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=6),
            preserve_default=False,
        ),
    ]