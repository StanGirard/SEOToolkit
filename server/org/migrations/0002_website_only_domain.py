# Generated by Django 3.1.4 on 2020-12-22 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('org', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='website',
            name='only_domain',
            field=models.BooleanField(default=False),
        ),
    ]