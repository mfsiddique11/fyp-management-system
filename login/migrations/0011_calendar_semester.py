# Generated by Django 2.1.7 on 2019-03-20 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0010_auto_20190320_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='calendar',
            name='semester',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]