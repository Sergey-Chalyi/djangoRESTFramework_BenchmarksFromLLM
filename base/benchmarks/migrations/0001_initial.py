# Generated by Django 5.1.2 on 2024-11-26 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Benchmark',
            fields=[
                ('request_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('prompt_text', models.TextField()),
                ('generated_text', models.TextField()),
                ('token_count', models.IntegerField()),
                ('time_to_first_token', models.IntegerField()),
                ('time_per_output_token', models.IntegerField()),
                ('total_generation_time', models.IntegerField()),
                ('timestamp', models.DateTimeField()),
            ],
        ),
    ]
