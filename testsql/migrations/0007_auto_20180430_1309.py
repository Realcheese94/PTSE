# Generated by Django 2.0.2 on 2018-04-30 04:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testsql', '0006_usercalendar'),
    ]

    operations = [
        migrations.AddField(
            model_name='nuser',
            name='Chargeuser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='testsql.SUser'),
        ),
        migrations.AlterField(
            model_name='usercalendar',
            name='Userid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='testsql.SUser'),
        ),
    ]
