# Generated by Django 5.0.7 on 2025-02-03 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0002_alter_work_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
