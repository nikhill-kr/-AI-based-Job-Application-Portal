# Generated by Django 2.2 on 2019-09-05 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_auto_20190905_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicants',
            name='phone',
            field=models.CharField(max_length=14),
        ),
    ]
