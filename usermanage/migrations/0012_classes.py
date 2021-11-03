# Generated by Django 3.2 on 2021-10-29 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermanage', '0011_rename_indentity_users_identity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='班级名')),
                ('owner', models.CharField(max_length=18, verbose_name='任课教师')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='上传时间')),
                ('subject', models.IntegerField(choices=[(0, 'Math'), (1, 'Further Math'), (2, 'Computer Science'), (3, 'English'), (4, 'Integrated English'), (5, 'Physics'), (6, 'Biology'), (7, 'Chemistry'), (8, 'Economics'), (9, 'Business'), (10, 'Psychology'), (11, '语文'), (12, '历史'), (13, '政治'), (14, '地理'), (15, '未知')], default=15, verbose_name='科目')),
                ('member', models.CharField(max_length=280, verbose_name='班级成员')),
            ],
        ),
    ]