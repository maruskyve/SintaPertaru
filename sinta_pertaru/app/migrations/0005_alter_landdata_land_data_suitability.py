# Generated by Django 4.1 on 2022-12-16 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_landdata_land_data_suitability'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landdata',
            name='land_data_suitability',
            field=models.CharField(max_length=90),
        ),
    ]