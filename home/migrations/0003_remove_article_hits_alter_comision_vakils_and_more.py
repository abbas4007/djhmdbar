# Generated by Django 5.1.4 on 2024-12-19 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_comision_vakils'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='hits',
        ),
        migrations.AlterField(
            model_name='comision',
            name='vakils',
            field=models.ManyToManyField(blank=True, null=True, related_name='comisions', to='home.vakil'),
        ),
        migrations.DeleteModel(
            name='ArticleHit',
        ),
        migrations.DeleteModel(
            name='IPAddress',
        ),
    ]