# Generated by Django 2.0.2 on 2018-04-09 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testsql', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='suser',
            name='Sinfo',
            field=models.TextField(blank=True, null=True),
        ),
    ]
