# Generated by Django 5.1.2 on 2024-10-23 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('markets', '0003_market_market_format_market_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='market',
            name='market_orientation',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
