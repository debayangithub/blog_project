# Generated by Django 2.1.6 on 2019-03-24 06:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20190323_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 24, 6, 56, 1, 502592, tzinfo=utc)),
        ),
    ]
