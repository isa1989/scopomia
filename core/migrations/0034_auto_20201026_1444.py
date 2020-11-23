# Generated by Django 2.0 on 2020-10-26 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0033_auto_20201026_1437'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='items',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='item',
        ),
        migrations.AddField(
            model_name='about',
            name='content_az',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='content_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='title_az',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='title_en',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='brendcategory',
            name='name_az',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='brendcategory',
            name='name_en',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='partnyor',
            name='content_az',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='partnyor',
            name='content_en',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='partnyor',
            name='title_az',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='partnyor',
            name='title_en',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]