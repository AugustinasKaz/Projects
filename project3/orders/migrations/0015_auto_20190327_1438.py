# Generated by Django 2.0.3 on 2019-03-27 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_auto_20190327_0610'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='date_posted',
        ),
        migrations.AlterField(
            model_name='order',
            name='topping_number_allowed',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='topps',
            field=models.ManyToManyField(to='orders.Topping'),
        ),
    ]