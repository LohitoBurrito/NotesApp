# Generated by Django 4.0.5 on 2022-07-21 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FrontPage', '0007_contributors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileupload',
            name='file',
            field=models.FileField(upload_to='files/'),
        ),
    ]
