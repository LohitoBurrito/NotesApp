# Generated by Django 4.0.6 on 2022-07-17 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FrontPage', '0004_delete_aero_course_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='fileUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseTag', models.CharField(max_length=100)),
                ('courseNum', models.CharField(max_length=3)),
                ('name', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='')),
            ],
        ),
    ]