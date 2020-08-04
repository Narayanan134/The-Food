# Generated by Django 3.0.5 on 2020-07-17 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20200715_1409'),
    ]

    operations = [
        migrations.AddField(
            model_name='breakfastt',
            name='dosaimg',
            field=models.ImageField(default=0, upload_to='pics'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='breakfastt',
            name='idliimg',
            field=models.ImageField(default=0, upload_to='pics'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='breakfastt',
            name='pongimg',
            field=models.ImageField(default=0, upload_to='pics'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='breakfastt',
            name='pooriimg',
            field=models.ImageField(default=0, upload_to='pics'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='breakfastt',
            name='upmaimg',
            field=models.ImageField(default=0, upload_to='pics'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='breakfastt',
            name='uthimg',
            field=models.ImageField(default=0, upload_to='pics'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dinnerr',
            name='dosaimg',
            field=models.ImageField(default=0, upload_to='pics'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dinnerr',
            name='idliimg',
            field=models.ImageField(default=0, upload_to='pics'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dinnerr',
            name='pongimg',
            field=models.ImageField(default=0, upload_to='pics'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dinnerr',
            name='pooriimg',
            field=models.ImageField(default=0, upload_to='pics'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dinnerr',
            name='upmaimg',
            field=models.ImageField(default=0, upload_to='pics'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dinnerr',
            name='uthimg',
            field=models.ImageField(default=0, upload_to='pics'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lunchh',
            name='curdimg',
            field=models.ImageField(default=0, upload_to='pics'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lunchh',
            name='dalimg',
            field=models.ImageField(default=0, upload_to='pics'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lunchh',
            name='lemimg',
            field=models.ImageField(default=0, upload_to='pics'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lunchh',
            name='tamimg',
            field=models.ImageField(default=0, upload_to='pics'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lunchh',
            name='vrimg',
            field=models.ImageField(default=0, upload_to='pics'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='breakfastt',
            name='qtyd',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='breakfastt',
            name='qtyi',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='breakfastt',
            name='qtypon',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='breakfastt',
            name='qtypoo',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='breakfastt',
            name='qtyth',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='breakfastt',
            name='qtyup',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='dinnerr',
            name='qtyd',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='dinnerr',
            name='qtyi',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='dinnerr',
            name='qtypon',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='dinnerr',
            name='qtypoo',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='dinnerr',
            name='qtyth',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='dinnerr',
            name='qtyup',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='lunchh',
            name='qtycurd',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='lunchh',
            name='qtydal',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='lunchh',
            name='qtylem',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='lunchh',
            name='qtytam',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='lunchh',
            name='qtyvr',
            field=models.IntegerField(),
        ),
    ]
