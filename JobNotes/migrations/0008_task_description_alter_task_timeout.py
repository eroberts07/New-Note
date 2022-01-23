# Generated by Django 4.0.1 on 2022-01-23 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobNotes', '0007_task_job_tasks'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='timeout',
            field=models.DateTimeField(blank=True),
        ),
    ]