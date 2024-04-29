# Generated by Django 5.0.4 on 2024-04-29 08:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics_platform', '0002_remove_data_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnalysisResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analytics_platform.data')),
            ],
        ),
    ]
