# Generated by Django 2.0.2 on 2018-02-22 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SentryModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('login', models.CharField(max_length=100)),
                ('first_name', models.CharField(blank=True, max_length=250, null=True)),
                ('last_name', models.CharField(blank=True, max_length=250, null=True)),
                ('email', models.EmailField(blank=True, max_length=100, null=True)),
                ('feature', models.CharField(blank=True, max_length=250, null=True)),
                ('org_id', models.BigIntegerField(null=True)),
                ('access_mode', models.DateField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]