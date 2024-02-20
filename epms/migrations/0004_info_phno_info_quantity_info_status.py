# Generated by Django 4.0.4 on 2022-04-29 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epms', '0003_admin'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='PhNo',
            field=models.IntegerField(default=12345),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='info',
            name='Quantity',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='info',
            name='Status',
            field=models.CharField(default='Replaced', max_length=20),
            preserve_default=False,
        ),
    ]