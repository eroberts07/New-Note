# Generated by Django 4.0.1 on 2022-01-25 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobNotes', '0020_active_remove_job_my_jobs_job_active_jobs'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
