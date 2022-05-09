# Generated by Django 4.0.4 on 2022-05-07 09:08

import django.core.validators
from django.db import migrations, models
import store.models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_alter_book_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='publish_year',
            field=models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1984), store.models.max_value_current_year], verbose_name='publish_year'),
        ),
    ]
