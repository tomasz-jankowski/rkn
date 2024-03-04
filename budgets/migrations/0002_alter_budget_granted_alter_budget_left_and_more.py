# Generated by Django 5.0.2 on 2024-03-04 14:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('budgets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='granted',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='budget',
            name='left',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='budget',
            name='requested',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12),
        ),
        migrations.AlterField(
            model_name='budget',
            name='spent',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=12),
        ),
    ]