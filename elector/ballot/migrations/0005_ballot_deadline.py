# Generated by Django 3.0.8 on 2020-07-25 15:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ballot', '0004_auto_20200725_1514'),
    ]

    operations = [
        migrations.AddField(
            model_name='ballot',
            name='deadline',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
