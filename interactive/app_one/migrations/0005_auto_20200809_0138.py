# Generated by Django 2.2 on 2020-08-09 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_one', '0004_auto_20200809_0050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postimage',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='images/'),
        ),
    ]
