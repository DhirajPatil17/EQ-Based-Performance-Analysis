# Generated by Django 4.0.5 on 2022-07-02 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myhome', '0003_syit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Profile_pic', models.ImageField(upload_to='')),
                ('desc', models.CharField(max_length=300)),
            ],
        ),
    ]
