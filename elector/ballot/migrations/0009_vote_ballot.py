# Generated by Django 3.0.8 on 2020-07-25 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ballot', '0008_auto_20200725_1811'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='ballot',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ballot.Ballot'),
            preserve_default=False,
        ),
    ]
