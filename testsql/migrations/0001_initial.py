# Generated by Django 2.0.2 on 2018-03-23 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SuserId', models.CharField(max_length=10)),
                ('Suserpw', models.CharField(max_length=10)),
                ('Susername', models.CharField(max_length=5)),
                ('Susertel', models.CharField(max_length=11)),
                ('Sinfo', models.TextField(null=True)),
            ],
        ),
    ]