# Generated by Django 2.2.19 on 2023-01-29 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20230129_1913'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='pub_date',
            new_name='date_added',
        ),
    ]
