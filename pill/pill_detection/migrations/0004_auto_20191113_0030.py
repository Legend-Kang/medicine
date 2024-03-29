# Generated by Django 2.2.1 on 2019-11-12 15:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pill_detection', '0003_auto_20191112_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='author',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, related_name='user_photos', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(default='no_image.jpg', upload_to='%d'),
        ),
    ]
