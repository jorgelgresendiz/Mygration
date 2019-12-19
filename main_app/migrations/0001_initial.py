# Generated by Django 2.2.6 on 2019-12-19 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Residence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_line_1', models.CharField(max_length=100)),
                ('address_line_2', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('latitude', models.IntegerField()),
                ('longitude', models.IntegerField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Workplace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_line_1', models.CharField(max_length=100)),
                ('address_line_2', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('latitude', models.IntegerField()),
                ('longitude', models.IntegerField()),
                ('company_name', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('employer_name', models.CharField(max_length=50)),
                ('employer_number', models.IntegerField()),
                ('employer_email', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
            ],
        ),
    ]
