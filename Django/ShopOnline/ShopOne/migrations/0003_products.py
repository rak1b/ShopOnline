# Generated by Django 3.1.1 on 2020-10-13 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShopOne', '0002_auto_20201013_1845'),
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=50)),
                ('product_desc', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField()),
                ('category', models.CharField(max_length=50)),
                ('sub_category', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='shop/imgs')),
            ],
        ),
    ]