# Generated by Django 4.1.7 on 2023-09-29 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_remove_rss_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='tag',
        ),
    ]
