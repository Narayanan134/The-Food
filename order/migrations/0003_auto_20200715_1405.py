# Generated by Django 3.0.5 on 2020-07-15 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20200715_1334'),
    ]

    operations = [
        migrations.CreateModel(
            name='breakfastt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Idli', models.BooleanField()),
                ('qtyi', models.IntegerField()),
                ('Dosa', models.BooleanField()),
                ('qtyd', models.IntegerField()),
                ('Pongal', models.BooleanField()),
                ('qtypon', models.IntegerField()),
                ('Uthapam', models.BooleanField()),
                ('qtyth', models.IntegerField()),
                ('Upma', models.BooleanField()),
                ('qtyup', models.IntegerField()),
                ('Poori', models.BooleanField()),
                ('qtypoo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='dinnerr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Idli', models.BooleanField()),
                ('qtyi', models.IntegerField()),
                ('Dosa', models.BooleanField()),
                ('qtyd', models.IntegerField()),
                ('Pongal', models.BooleanField()),
                ('qtypon', models.IntegerField()),
                ('Uthapam', models.BooleanField()),
                ('qtyth', models.IntegerField()),
                ('Upma', models.BooleanField()),
                ('qtyup', models.IntegerField()),
                ('Poori', models.BooleanField()),
                ('qtypoo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='lunchh',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Curd', models.BooleanField()),
                ('qtycurd', models.IntegerField()),
                ('Dal', models.BooleanField()),
                ('qtydal', models.IntegerField()),
                ('Lemon', models.BooleanField()),
                ('qtylem', models.IntegerField()),
                ('Tamarind', models.BooleanField()),
                ('qtytam', models.IntegerField()),
                ('Vegrice', models.BooleanField()),
                ('qtyvr', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='breakfast',
        ),
        migrations.DeleteModel(
            name='dinner',
        ),
        migrations.DeleteModel(
            name='lunch',
        ),
    ]