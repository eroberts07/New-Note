# Generated by Django 4.0.1 on 2022-01-23 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobNotes', '0004_rename_equipment_job_equipment'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='active',
            field=models.ManyToManyField(related_name='active_jobs', to='JobNotes.User'),
        ),
    ]
