# Generated by Django 2.0.2 on 2018-02-20 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MedicalList',
            fields=[
                ('active', models.BooleanField(default=True)),
                ('modified', models.DateField(auto_now=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('composition', models.CharField(max_length=250)),
                ('reimbursible', models.CharField(max_length=100)),
                ('usage', models.CharField(max_length=250)),
                ('comments', models.CharField(max_length=250)),
                ('app_date', models.DateField(auto_now=True)),
                ('link', models.URLField(max_length=250)),
            ],
            options={
                'ordering': ['-active', 'app_date'],
            },
        ),
    ]