# Generated by Django 3.1.4 on 2020-12-22 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_organization_work'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organization',
            name='disciplines_list',
        ),
        migrations.RemoveField(
            model_name='organization',
            name='score',
        ),
        migrations.AddField(
            model_name='organization',
            name='school',
            field=models.CharField(blank=True, max_length=80, null=True, verbose_name='Школа'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='min_score',
            field=models.TextField(blank=True, null=True, verbose_name='Прочее json'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Название направления'),
        ),
    ]