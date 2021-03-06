# Generated by Django 3.0.5 on 2020-04-22 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('seats', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Varsity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('loaction', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('designation', models.CharField(max_length=200)),
                ('years_of_service', models.IntegerField()),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to='demo.Department')),
                ('varsity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to='demo.Varsity')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('reg_no', models.IntegerField()),
                ('session', models.CharField(choices=[('2016-17', '2016-17'), ('2017-18', '2017-18'), ('2018-19', '2018-19'), ('2019-20', '2019-20')], max_length=200)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='demo.Department')),
                ('varsity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='demo.Varsity')),
            ],
        ),
    ]
