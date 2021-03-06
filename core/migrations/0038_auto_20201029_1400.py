# Generated by Django 2.0 on 2020-10-29 14:00

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0037_auto_20201028_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='item',
            name='description_az',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='description_ru',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='specification',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='item',
            name='specification_az',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='specification_ru',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
