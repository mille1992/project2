# Generated by Django 3.1.2 on 2020-12-17 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auto_20201205_1041'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='listingStatus',
            field=models.CharField(default='open', max_length=64),
        ),
    ]
