# Generated by Django 5.0.7 on 2024-12-01 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddressManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True, null=True)),
                ('updated_datetime', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('Permanent_address', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('pincode', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'address',
                'verbose_name_plural': 'address',
                'db_table': 'manager_address',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='BackgroundManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True, null=True)),
                ('updated_datetime', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('educational_qualifications', models.CharField(blank=True, max_length=100, null=True)),
                ('previous_details', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'background',
                'verbose_name_plural': 'backgrounds',
                'db_table': 'manager_background',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='BenefitsManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True, null=True)),
                ('updated_datetime', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('salary_details', models.CharField(blank=True, max_length=100, null=True)),
                ('bank_name', models.CharField(blank=True, max_length=100, null=True)),
                ('account_number', models.IntegerField(blank=True, null=True)),
                ('branch_name', models.CharField(blank=True, max_length=100, null=True)),
                ('ifsc_code', models.CharField(blank=True, max_length=100, null=True)),
                ('pancard', models.CharField(blank=True, max_length=100, null=True)),
                ('pancard_file', models.FileField(blank=True, null=True, upload_to='')),
                ('pf_fund', models.FloatField(default=0)),
                ('state_insurance_number', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'benefits',
                'verbose_name_plural': 'benefit',
                'db_table': 'manager_benefits',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='EmergencyContactManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True, null=True)),
                ('updated_datetime', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('Permanent_address', models.CharField(blank=True, max_length=100, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('pincode', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'contact',
                'verbose_name_plural': 'contacts',
                'db_table': 'manager_contact',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='IdentificationManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True, null=True)),
                ('updated_datetime', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('employe_type', models.CharField(blank=True, choices=[('AD', 'ADHAAR'), ('PS', 'PASSPORT'), ('SSN', ' SOCIAL SECURITY NUMBER (US)')], max_length=100, null=True)),
                ('work_authorization', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'work_schedule',
                'verbose_name_plural': 'work_schedules',
                'db_table': 'manager_work_schedule',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True, null=True)),
                ('updated_datetime', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('department', models.CharField(blank=True, max_length=100, null=True)),
                ('designation', models.CharField(blank=True, max_length=100, null=True)),
                ('date_of_joining', models.DateField(blank=True, null=True)),
                ('employment_Type', models.CharField(blank=True, choices=[('FT', 'FULL TIME'), ('PT', 'PART TIME'), ('CT', 'CONTRACT'), ('FR', 'FREELANCE')], max_length=100, null=True)),
                ('reporting_manager', models.CharField(blank=True, max_length=100, null=True)),
                ('work_location', models.CharField(blank=True, max_length=100, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
            options={
                'verbose_name': 'manager',
                'verbose_name_plural': 'managers',
                'db_table': 'manager_manager',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='SkillManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True, null=True)),
                ('updated_datetime', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('skill', models.CharField()),
            ],
            options={
                'verbose_name': ' skill',
                'verbose_name_plural': ' skills',
                'db_table': 'manager_ skill',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='WorkScheduleManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(auto_now_add=True, null=True)),
                ('updated_datetime', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('end_time', models.TimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Identification',
                'verbose_name_plural': 'Identificationss',
                'db_table': 'manager_Identification',
                'ordering': ['-id'],
            },
        ),
    ]