# Generated by Django 3.1.4 on 2021-01-02 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('org', '0002_website_only_domain'),
        ('lighthouse', '0011_auto_20201227_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='lighthouse',
            name='org',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, related_name='ligthouse', to='org.website'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lighthouse_result',
            name='org',
            field=models.ForeignKey(default='5', on_delete=django.db.models.deletion.CASCADE, related_name='ligthouse_results_org', to='org.website'),
            preserve_default=False,
        ),
    ]
