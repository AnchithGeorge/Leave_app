# Generated by Django 5.0.7 on 2025-01-01 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_managers'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='otp',
            options={'ordering': ['-id'], 'verbose_name': 'OTP', 'verbose_name_plural': 'OTPs'},
        ),
    ]
