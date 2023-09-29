# Generated by Django 4.1.7 on 2023-09-29 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_remove_tag_category_delete_contentcat_delete_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentCat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(default=None, max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(default=None, verbose_name='Comment'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.CharField(default=None, max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(default=None, verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='post',
            name='preview',
            field=models.CharField(default=None, max_length=5000),
        ),
        migrations.AlterField(
            model_name='rss',
            name='content',
            field=models.TextField(default=None, verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='rss',
            name='date_posted',
            field=models.DateTimeField(default=None),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(default=None, max_length=100)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.contentcat')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='blog.tag'),
        ),
        migrations.AddField(
            model_name='rss',
            name='tag',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='blog.tag'),
        ),
    ]
