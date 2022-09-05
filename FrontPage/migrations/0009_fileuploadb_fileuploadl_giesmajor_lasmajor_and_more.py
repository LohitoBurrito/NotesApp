# Generated by Django 4.0.5 on 2022-07-23 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FrontPage', '0008_alter_fileupload_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='fileUploadB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseTag', models.CharField(max_length=100)),
                ('courseNum', models.CharField(max_length=3)),
                ('name', models.CharField(max_length=100)),
                ('creator', models.CharField(default='', max_length=100)),
                ('file', models.FileField(upload_to='files/')),
            ],
        ),
        migrations.CreateModel(
            name='fileUploadL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseTag', models.CharField(max_length=100)),
                ('courseNum', models.CharField(max_length=3)),
                ('name', models.CharField(max_length=100)),
                ('creator', models.CharField(default='', max_length=100)),
                ('file', models.FileField(upload_to='files/')),
            ],
        ),
        migrations.CreateModel(
            name='giesMajor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='lasMajor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameModel(
            old_name='fileUpload',
            new_name='fileUploadG',
        ),
    ]
