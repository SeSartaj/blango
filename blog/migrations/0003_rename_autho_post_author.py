# Generated by Django 3.2.5 on 2022-01-07 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='autho',
            new_name='author',
        ),
    ]
