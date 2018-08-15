# Generated by Django 2.1 on 2018-08-15 05:41

from django.db import migrations, models
import image_api.models


class Migration(migrations.Migration):

    dependencies = [
        ('image_api', '0003_auto_20180815_0441'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='category',
            field=models.CharField(default='other', help_text='Category of Image', max_length=100),
        ),
        migrations.AddField(
            model_name='image',
            name='title',
            field=models.CharField(default='test', help_text='Title of Image', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='image',
            name='creation_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='image',
            name='name',
            field=models.CharField(editable=False, help_text='Name of Image', max_length=100),
        ),
        migrations.AlterField(
            model_name='image',
            name='publish_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='image',
            name='source_large',
            field=models.ImageField(blank=True, help_text='URL of the image location (S3... etc.)', upload_to=image_api.models.file_path),
        ),
        migrations.AlterField(
            model_name='image',
            name='source_small',
            field=models.ImageField(blank=True, help_text='URL of the image location (S3... etc.)', upload_to=image_api.models.file_path),
        ),
        migrations.AlterField(
            model_name='image',
            name='source_standard',
            field=models.ImageField(help_text='URL of the image location (S3... etc.)', upload_to=image_api.models.file_path),
        ),
    ]