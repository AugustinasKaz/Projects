# Generated by Django 2.0.3 on 2019-03-25 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0009_auto_20190325_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='topping_number',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]