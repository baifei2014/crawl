# Generated by Django 2.2.7 on 2019-11-23 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rouse', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='url',
            new_name='path',
        ),
        migrations.RenameField(
            model_name='image',
            old_name='artical_id',
            new_name='schedule_id',
        ),
        migrations.AddField(
            model_name='image',
            name='name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
