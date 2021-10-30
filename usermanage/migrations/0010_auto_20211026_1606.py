# Generated by Django 3.2 on 2021-10-26 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermanage', '0009_files_publish'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='indentity',
            field=models.IntegerField(choices=[(1, '学生'), (2, '教师')], default=1, verbose_name='身份'),
        ),
        migrations.AlterField(
            model_name='files',
            name='uploaded_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='上传时间'),
        ),
    ]
