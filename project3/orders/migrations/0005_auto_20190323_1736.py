# Generated by Django 2.0.3 on 2019-03-23 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_order_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Regular_Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ptype', models.CharField(max_length=64)),
                ('price', models.FloatField(null=True)),
                ('size', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='regular_pizza',
            name='topps',
            field=models.ManyToManyField(blank=True, related_name='Regular_Pizza', to='orders.Topping'),
        ),
    ]
