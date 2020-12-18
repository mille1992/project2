# Generated by Django 3.1.2 on 2020-12-17 20:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_listing_listingstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='listing',
            field=models.ForeignKey(default='9', on_delete=django.db.models.deletion.CASCADE, related_name='ListingsCommenters', to='auctions.listing'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='commentCreator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentingUsers', to=settings.AUTH_USER_MODEL),
        ),
    ]