# Generated by Django 4.0.3 on 2023-04-22 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_dealer_portal', '0003_vehicles_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicles',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
