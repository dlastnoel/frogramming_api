# Generated by Django 3.2.3 on 2021-06-09 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_module_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='description',
            field=models.TextField(max_length=255),
        ),
    ]
