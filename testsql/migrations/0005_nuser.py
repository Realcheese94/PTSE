# Generated by Django 2.0.2 on 2018-04-30 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testsql', '0004_auto_20180409_1412'),
    ]

    operations = [
        migrations.CreateModel(
            name='NUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NUsername', models.CharField(max_length=10)),
            ],
        ),
    ]
