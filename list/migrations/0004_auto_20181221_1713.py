# Generated by Django 2.1.4 on 2018-12-21 17:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0003_auto_20181221_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='cdate',
            field=models.DateField(default=datetime.datetime(2018, 12, 21, 17, 13, 34, 779451, tzinfo=utc)),
        ),
    ]
