# Generated by Django 2.0 on 2020-09-26 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_settings_slider_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='slider_content_1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='settings',
            name='slider_content_2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='settings',
            name='slider_image_1',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='settings',
            name='slider_image_2',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='settings',
            name='slider_title_1',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='settings',
            name='slider_title_2',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]