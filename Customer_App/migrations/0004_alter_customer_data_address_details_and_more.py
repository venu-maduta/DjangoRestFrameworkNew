# Generated by Django 4.1.1 on 2022-09-07 21:13

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Customer_App', '0003_customer_data_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_data',
            name='address_details',
            field=jsonfield.fields.JSONField(default={}),
        ),
        migrations.AlterField(
            model_name='customer_data',
            name='workExperience',
            field=jsonfield.fields.JSONField(default={}),
        ),
    ]