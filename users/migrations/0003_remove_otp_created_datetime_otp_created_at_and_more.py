# Generated by Django 5.0.7 on 2024-12-24 04:13

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_email_alter_user_gender_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='otp',
            name='created_datetime',
        ),
        migrations.AddField(
            model_name='otp',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='otp',
            name='otp',
            field=models.CharField(max_length=6),
        ),
    ]
