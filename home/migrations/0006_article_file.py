# Generated by Django 5.1.4 on 2025-01-14 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_article_author_alter_article_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
