# Generated by Django 2.0.4 on 2018-06-10 10:29

import chigre.models.common
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chigre', '0009_beer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('pintprice', models.DecimalField(decimal_places=2, max_digits=5)),
                ('canyaprice', models.DecimalField(decimal_places=2, max_digits=5)),
                ('fullweight', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('emptyweight', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('actualweight', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('beer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chigre.Beer')),
                ('creator', models.ForeignKey(on_delete=models.SET(chigre.models.common.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
                ('kegtype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chigre.KegType')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]