# Generated by Django 3.2.3 on 2021-05-30 20:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_todo_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='group',
            field=models.TextField(default='home'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 30, 23, 21, 51, 770297)),
        ),
    ]
