# Generated by Django 3.2.7 on 2021-09-02 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='detection_fingures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input_Main_Img', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
