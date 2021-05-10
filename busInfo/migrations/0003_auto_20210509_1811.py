# Generated by Django 3.0.3 on 2021-05-09 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busInfo', '0002_auto_20210509_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stopname',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=22, null=True),
        ),
        migrations.AlterField(
            model_name='stopname',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=10, max_digits=22, null=True),
        ),
    ]
