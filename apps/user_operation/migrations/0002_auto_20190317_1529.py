# Generated by Django 2.1.7 on 2019-03-17 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_operation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='signer_mobile',
            field=models.CharField(default='', max_length=50, verbose_name='电话'),
        ),
    ]
