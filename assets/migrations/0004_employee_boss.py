# Generated by Django 2.0.2 on 2018-03-05 04:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0003_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='boss',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='assets.Employee'),
        ),
    ]