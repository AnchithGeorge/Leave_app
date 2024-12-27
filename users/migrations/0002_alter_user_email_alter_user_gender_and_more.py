# Generated by Django 5.0.7 on 2024-12-23 03:32

import django.core.validators
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, error_messages={'unique': 'Email already used'}, max_length=255, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='O', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='maritul_status',
            field=models.CharField(blank=True, choices=[('SI', 'SINGILE'), ('MA', 'MARRIED'), ('OT', 'OTHER')], default='OT', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator('^\\+?1?\\d{9,15}$', "Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")]),
        ),
    ]