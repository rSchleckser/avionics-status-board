# Generated by Django 5.0.7 on 2025-02-03 22:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0003_work_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airplane',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line_number', models.IntegerField(unique=True)),
                ('effectivity', models.IntegerField()),
                ('customer', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='work',
            name='airplane',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='work.airplane'),
            preserve_default=False,
        ),
    ]
