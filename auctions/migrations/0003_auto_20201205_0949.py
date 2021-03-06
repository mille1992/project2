# Generated by Django 3.1.2 on 2020-12-05 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_bid_comment_listing'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='bidingUser',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='bidder', to='auctions.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comment',
            name='commentCreator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='commenter', to='auctions.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='listingOwner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='listingCreator', to='auctions.user'),
            preserve_default=False,
        ),
    ]
