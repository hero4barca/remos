# Generated by Django 5.1.4 on 2025-01-16 12:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0011_alter_podcastepisodepage_episode_thumbnail_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='podcastepisodepage',
            name='date',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2025, 1, 16, 12, 52, 35, 80002, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
