# Generated by Django 4.0.4 on 2022-04-29 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('epms', '0002_registrations_phno'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('PassWord', models.TextField()),
            ],
        ),
    ]
