# Generated by Django 3.1.7 on 2021-03-11 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20210311_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlink',
            name='qr_img',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
