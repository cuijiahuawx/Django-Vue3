# Generated by Django 3.1.14 on 2022-05-31 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_musicid'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='musicEmail',
            field=models.EmailField(blank=True, max_length=50, null=True, unique=True, verbose_name='音乐邮箱'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
