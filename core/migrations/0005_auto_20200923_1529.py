# Generated by Django 2.0 on 2020-09-23 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='images/')),
            ],
        ),
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='itemimage',
            name='post',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='core.Item'),
        ),
    ]
