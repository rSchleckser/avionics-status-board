# Generated by Django 5.0.7 on 2025-02-04 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airplane', '0003_airplane_created_at_airplane_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='airplane',
            name='location_city',
            field=models.CharField(choices=[('renton', 'Renton'), ('seattle', 'Seattle'), ('everett', 'Everett'), ('moses_lake', 'Moses Lake'), ('victorville', 'Victorville'), ('portland', 'Portland'), ('china', 'China'), ('other', 'Other')], default='seattle', max_length=50),
        ),
        migrations.AddField(
            model_name='airplane',
            name='location_stall',
            field=models.CharField(blank=True, choices=[('C3', 'C3'), ('C4', 'C4'), ('C5', 'C5'), ('C6', 'C6'), ('C7', 'C7'), ('C8', 'C8'), ('C9', 'C9'), ('C10', 'C10'), ('C11', 'C11'), ('C12', 'C12'), ('C13', 'C13'), ('C14', 'C14'), ('C15', 'C15'), ('C16', 'C16'), ('C17', 'C17'), ('C18', 'C18'), ('C19', 'C19'), ('C20', 'C20'), ('B3', 'B3'), ('B4', 'B4'), ('B5', 'B5'), ('B6', 'B6'), ('B7', 'B7'), ('B8', 'B8'), ('B9', 'B9'), ('B10', 'B10'), ('B11', 'B11'), ('B12', 'B12'), ('B13', 'B13'), ('B14', 'B14'), ('B15', 'B15'), ('B16', 'B16'), ('B3N', 'B3N'), ('B3S', 'B3S'), ('B4N', 'B4N'), ('B4S', 'B4S')], max_length=10, null=True),
        ),
    ]
