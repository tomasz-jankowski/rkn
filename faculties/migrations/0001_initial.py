# Generated by Django 5.0.2 on 2024-03-04 12:56

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(unique=True)),
                ('slug', models.SlugField(blank=True, editable=False)),
            ],
            options={
                'verbose_name_plural': 'faculties',
                'db_table': 'faculties',
            },
        ),
    ]