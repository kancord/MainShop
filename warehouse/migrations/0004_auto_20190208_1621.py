# Generated by Django 2.1.5 on 2019-02-08 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('warehouse', '0003_auto_20190207_1815'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='decsription',
            new_name='description',
        ),
    ]
