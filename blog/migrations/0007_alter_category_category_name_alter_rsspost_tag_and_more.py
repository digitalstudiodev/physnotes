# Generated by Django 4.1.7 on 2023-09-27 00:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_rsspost_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(default=1, max_length=100),
        ),
        migrations.AlterField(
            model_name='rsspost',
            name='tag',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='blog.tag'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tag_name',
            field=models.CharField(default=1, max_length=100),
        ),
    ]
