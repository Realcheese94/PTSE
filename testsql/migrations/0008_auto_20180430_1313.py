# Generated by Django 2.0.2 on 2018-04-30 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testsql', '0007_auto_20180430_1309'),
    ]

    operations = [
        migrations.AddField(
            model_name='usercalendar',
            name='Udate',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='usercalendar',
            name='Udoing',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='usercalendar',
            name='Uyear',
            field=models.IntegerField(null=True),
        ),
    ]
