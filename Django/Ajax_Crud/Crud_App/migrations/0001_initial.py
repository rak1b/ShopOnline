# Generated by Django 3.1.2 on 2020-11-02 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student_info',
            fields=[
                ('st_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=140)),
                ('pas', models.CharField(max_length=100)),
            ],
        ),
    ]
