# Generated by Django 4.1.7 on 2023-09-27 00:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_rename_tag_rsspost_rss_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rsspost',
            name='rss_tag',
        ),
    ]
