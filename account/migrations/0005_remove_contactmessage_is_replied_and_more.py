# Generated by Django 5.1.5 on 2025-02-10 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_remove_contactmessage_full_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactmessage',
            name='is_replied',
        ),
        migrations.RemoveField(
            model_name='contactmessage',
            name='name',
        ),
        migrations.RemoveField(
            model_name='contactmessage',
            name='reply_message',
        ),
        migrations.AddField(
            model_name='contactmessage',
            name='full_name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='نام کامل'),
        ),
        migrations.AddField(
            model_name='contactmessage',
            name='response',
            field=models.TextField(blank=True, null=True, verbose_name='پاسخ'),
        ),
        migrations.AddField(
            model_name='contactmessage',
            name='status',
            field=models.CharField(choices=[('pending', 'در انتظار پاسخ'), ('replied', 'پاسخ داده شده')], default='pending', max_length=10, verbose_name='وضعیت'),
        ),
        migrations.AlterField(
            model_name='contactmessage',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ارسال'),
        ),
        migrations.AlterField(
            model_name='contactmessage',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='ایمیل'),
        ),
        migrations.AlterField(
            model_name='contactmessage',
            name='message',
            field=models.TextField(verbose_name='پیام'),
        ),
        migrations.AlterField(
            model_name='contactmessage',
            name='phone',
            field=models.CharField(max_length=15, verbose_name='شماره تماس'),
        ),
        migrations.AlterField(
            model_name='contactmessage',
            name='subject',
            field=models.CharField(max_length=200, verbose_name='موضوع'),
        ),
    ]
