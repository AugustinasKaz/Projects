# Generated by Django 2.0.3 on 2019-05-14 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('love', '0002_calculator_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calculator',
            name='percentage',
            field=models.FloatField(null=True),
        ),
    ]
