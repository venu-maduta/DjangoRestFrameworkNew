# Generated by Django 4.1.1 on 2022-09-07 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer_App', '0002_alter_customer_data_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer_data',
            name='photo',
            field=models.CharField(blank=True, max_length=100000),
        ),
    ]