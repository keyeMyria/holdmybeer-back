# Generated by Django 2.0.6 on 2018-06-10 14:17

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('chigre', '0014_auto_20180610_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='brewery',
            name='country',
            field=django_countries.fields.CountryField(default='ES', max_length=2),
            preserve_default=False,
        ),
    ]
