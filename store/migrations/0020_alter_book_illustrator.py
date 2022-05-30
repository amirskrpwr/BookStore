# Generated by Django 4.0.3 on 2022-05-30 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0019_rename_illustrator_book_illustrator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='illustrator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='store.illustrator'),
        ),
    ]
