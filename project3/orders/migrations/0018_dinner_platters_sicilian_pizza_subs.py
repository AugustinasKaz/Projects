# Generated by Django 2.0.3 on 2019-03-28 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0017_auto_20190328_1538'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dinner_Platters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('small', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('large', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Sicilian_Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('small', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('large', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Subs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('small', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('large', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
            ],
        ),
    ]