# Generated by Django 4.0.1 on 2022-01-23 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JobNotes', '0016_alter_task_timeout'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='timein',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='timeout',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]