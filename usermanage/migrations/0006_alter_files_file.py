# Generated by Django 3.2 on 2021-10-25 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermanage', '0005_rename_sex_files_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='file',
            field=models.FileField(unique=True, upload_to='file'),
        ),
    ]
