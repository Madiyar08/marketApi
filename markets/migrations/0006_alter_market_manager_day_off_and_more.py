# Generated by Django 5.1.2 on 2024-10-23 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('markets', '0005_alter_market_market_work_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='market',
            name='manager_day_off',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='market',
            name='manager_full_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='market',
            name='manager_work_time',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='market',
            name='market_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='market',
            name='market_work_time',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
