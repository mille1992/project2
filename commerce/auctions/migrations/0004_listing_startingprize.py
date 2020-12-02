# Generated by Django 3.1.2 on 2020-12-02 20:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_listing_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='startingPrize',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0.01)]),
            preserve_default=False,
        ),
    ]
