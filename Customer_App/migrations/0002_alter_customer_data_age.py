# Generated by Django 4.1.1 on 2022-09-07 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer_App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_data',
            name='age',
            field=models.IntegerField(blank=True),
        ),
    ]
