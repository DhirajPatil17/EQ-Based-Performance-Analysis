# Generated by Django 4.0.5 on 2022-07-01 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myhome', '0002_fyit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Syit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Marks', models.IntegerField()),
                ('Attendence', models.IntegerField()),
                ('Behavioral', models.IntegerField()),
            ],
        ),
    ]