# Generated by Django 3.2.3 on 2021-06-09 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_module_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='type',
            field=models.CharField(choices=[('fill', 'Fill in the blanks'), ('choice', 'Multiple choice'), ('tf', 'True or False')], max_length=255),
        ),
    ]
