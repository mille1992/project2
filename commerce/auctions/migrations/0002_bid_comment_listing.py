# Generated by Django 3.1.2 on 2020-11-25 17:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bidPrize', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0.01)])),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commentContent', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('listingPrize', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(0.01)])),
                ('imageUrl', models.CharField(max_length=128)),
            ],
        ),
    ]