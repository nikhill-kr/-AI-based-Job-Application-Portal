# Generated by Django 2.2.4 on 2019-09-01 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Designation', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=2000)),
                ('Experience', models.CharField(max_length=100)),
                ('Skills', models.CharField(max_length=500)),
            ],
        ),
    ]
