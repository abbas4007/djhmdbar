# Generated by Django 5.1.5 on 2025-02-07 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_alter_article_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='riyasat',
            name='role',
            field=models.CharField(max_length=50, verbose_name='نقش'),
        ),
    ]
