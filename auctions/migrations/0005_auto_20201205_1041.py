# Generated by Django 3.1.2 on 2020-12-05 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_bid_listing'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bid',
            old_name='bidingUser',
            new_name='biddingUser',
        ),
    ]
