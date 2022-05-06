# Generated by Django 4.0.4 on 2022-05-05 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_remove_shippingaddress_date_added_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='city',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='state',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='ShippingAddress',
        ),
    ]
