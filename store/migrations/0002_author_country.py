# Generated by Django 4.0.4 on 2022-06-07 10:21

from django.db import migrations
import django.utils.timezone
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='country',
            field=django_countries.fields.CountryField(default=django.utils.timezone.now, max_length=2),
            preserve_default=False,
        ),
    ]
