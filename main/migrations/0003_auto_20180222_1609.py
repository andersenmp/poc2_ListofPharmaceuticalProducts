# Generated by Django 2.0.2 on 2018-02-22 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20180222_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sentrymodel',
            name='org_id',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
