# Generated by Django 3.1.2 on 2020-12-17 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_auto_20201217_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='listing',
            field=models.ForeignKey(default='9', on_delete=django.db.models.deletion.CASCADE, related_name='listingsCommenters', to='auctions.listing'),
        ),
    ]
