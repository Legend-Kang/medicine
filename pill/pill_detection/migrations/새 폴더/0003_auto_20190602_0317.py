# Generated by Django 2.2.1 on 2019-06-01 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pill_detection', '0002_auto_20190602_0307'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pill_db',
            options={},
        ),
        migrations.RemoveField(
            model_name='pill_db',
            name='created',
        ),
        migrations.RemoveField(
            model_name='pill_db',
            name='updated',
        ),
    ]
