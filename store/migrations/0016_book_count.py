# Generated by Django 4.0.3 on 2022-05-30 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_alter_book_price_alter_book_publisher'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='count',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
