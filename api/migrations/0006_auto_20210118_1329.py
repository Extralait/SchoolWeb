# Generated by Django 3.1.4 on 2021-01-18 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20210116_0640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.CharField(choices=[('parent', 'Родитель'), ('enrollee', 'Абитуриент')], max_length=12, verbose_name='Статус'),
        ),
    ]
