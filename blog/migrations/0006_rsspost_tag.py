# Generated by Django 4.1.7 on 2023-09-27 00:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_rsspost_date_posted'),
    ]

    operations = [
        migrations.AddField(
            model_name='rsspost',
            name='tag',
            field=models.ForeignKey(default='General', on_delete=django.db.models.deletion.DO_NOTHING, to='blog.tag'),
        ),
    ]
