# Generated by Django 4.2.5 on 2023-10-15 08:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='context',
            new_name='content',
        ),
        migrations.AddField(
            model_name='posts',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2023, 10, 15, 8, 40, 24, 287555), verbose_name='publish date'),
        ),
    ]
