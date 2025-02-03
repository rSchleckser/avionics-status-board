# Generated by Django 5.0.7 on 2025-02-03 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0004_airplane_work_airplane'),
    ]

    operations = [
        migrations.AddField(
            model_name='airplane',
            name='delivered',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='airplane',
            name='ticketed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='work',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('in_progress', 'In Progress'), ('completed', 'Completed'), ('cant_work', "Can't Work"), ('open_paper', 'Open Paper')], default='pending', max_length=50),
        ),
    ]
