# Generated by Django 3.0.5 on 2020-04-20 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0004_auto_20200420_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='dept',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='department', to='demo.Department'),
        ),
    ]
