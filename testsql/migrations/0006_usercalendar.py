# Generated by Django 2.0.2 on 2018-04-30 01:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testsql', '0005_nuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCalendar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Uyear', models.IntegerField()),
                ('Userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testsql.SUser')),
            ],
        ),
    ]