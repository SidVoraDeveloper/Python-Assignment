# Generated by Django 3.1.2 on 2020-10-06 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='image',
            field=models.ImageField(upload_to='employee_image'),
        ),
    ]