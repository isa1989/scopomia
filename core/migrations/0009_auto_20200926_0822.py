# Generated by Django 2.0 on 2020-09-26 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20200926_0703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='slider_content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
