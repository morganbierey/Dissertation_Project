# Generated by Django 2.1.5 on 2023-02-10 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('educational_tool', '0009_auto_20230210_0207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='upload_file',
            field=models.FileField(max_length=254, upload_to='C:\\Users\\biere\\OneDrive - University of Glasgow\\Documents\\y3 v2\\year 4\\individual project\\Dissertation_Project\\project\\individual_project\\media'),
        ),
    ]
