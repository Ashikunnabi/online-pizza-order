# Generated by Django 2.1.5 on 2019-01-24 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_app', '0003_auto_20190124_1918'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pizza',
            old_name='current_big_pizzaprice',
            new_name='current_big_pizzap_rice',
        ),
        migrations.RenameField(
            model_name='pizza',
            old_name='current_regular_pizzaprice',
            new_name='current_regular_pizza_price',
        ),
        migrations.RenameField(
            model_name='pizza',
            old_name='current_small_pizzaprice',
            new_name='current_small_pizza_price',
        ),
    ]
