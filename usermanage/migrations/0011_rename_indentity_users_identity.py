# Generated by Django 3.2 on 2021-10-26 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usermanage', '0010_auto_20211026_1606'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='indentity',
            new_name='identity',
        ),
    ]
