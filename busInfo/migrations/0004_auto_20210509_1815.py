# Generated by Django 3.0.3 on 2021-05-09 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busInfo', '0003_auto_20210509_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stopname',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='stopname',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
