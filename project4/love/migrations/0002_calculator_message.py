# Generated by Django 2.0.3 on 2019-05-14 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('love', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='calculator',
            name='message',
            field=models.TextField(blank=True),
        ),
    ]
