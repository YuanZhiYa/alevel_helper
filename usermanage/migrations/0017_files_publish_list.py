# Generated by Django 3.2 on 2021-11-04 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermanage', '0016_alter_files_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='files',
            name='publish_list',
            field=models.CharField(default='', max_length=900, verbose_name='公开列表'),
        ),
    ]