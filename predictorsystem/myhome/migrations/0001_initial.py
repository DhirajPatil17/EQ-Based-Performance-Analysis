# Generated by Django 4.0.5 on 2022-06-11 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='visualize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Marks', models.IntegerField()),
                ('Attendence', models.IntegerField()),
                ('Behavioral', models.IntegerField()),
            ],
        ),
    ]
