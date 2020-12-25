# Generated by Django 3.1.4 on 2020-12-25 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20201226_0323'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='date',
        ),
        migrations.AlterField(
            model_name='event',
            name='link',
            field=models.CharField(db_index=True, max_length=200, unique=True, verbose_name='Ссылка'),
        ),
    ]