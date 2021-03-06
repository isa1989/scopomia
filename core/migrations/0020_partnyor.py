# Generated by Django 2.0 on 2020-10-09 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_remove_item_parent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partnyor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('image', models.FileField(blank=True, upload_to='')),
                ('url', models.URLField(max_length=255)),
            ],
        ),
    ]
