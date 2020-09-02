# Generated by Django 3.1 on 2020-08-31 03:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryName', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parkingNumber', models.CharField(max_length=20, null=True)),
                ('vehicleComapny', models.CharField(max_length=20, null=True)),
                ('regNo', models.CharField(max_length=20, null=True)),
                ('ownerName', models.CharField(max_length=20, null=True)),
                ('ownerContact', models.CharField(max_length=20, null=True)),
                ('inTime', models.CharField(max_length=20, null=True)),
                ('outTime', models.CharField(max_length=20, null=True)),
                ('parkingCharge', models.CharField(max_length=20, null=True)),
                ('remark', models.CharField(max_length=200, null=True)),
                ('status', models.CharField(max_length=200, null=True)),
                ('pdate', models.DateField(auto_now_add=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VPM.category')),
            ],
        ),
    ]
