# Generated by Django 4.1.7 on 2023-09-27 00:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_alter_rsspost_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rsspost',
            old_name='tag',
            new_name='rss_tag',
        ),
    ]
