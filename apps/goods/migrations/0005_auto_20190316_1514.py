# Generated by Django 2.1.7 on 2019-03-16 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_hotsearchwords'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goodsimage',
            old_name='iamge',
            new_name='image',
        ),
    ]
