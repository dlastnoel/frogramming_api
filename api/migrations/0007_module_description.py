# Generated by Django 3.2.3 on 2021-06-09 07:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20210605_0024'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='description',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]
