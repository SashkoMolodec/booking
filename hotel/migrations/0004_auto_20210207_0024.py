# Generated by Django 3.1.6 on 2021-02-06 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0003_auto_20210207_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='capacity',
            field=models.DecimalField(decimal_places=0, max_digits=1000),
        ),
    ]
