# Generated by Django 4.0.3 on 2022-05-30 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0020_alter_book_illustrator'),
    ]

    operations = [
        migrations.AddField(
            model_name='publisher',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='publisher',
            name='birth_place',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
