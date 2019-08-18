# Generated by Django 2.2.1 on 2019-08-17 23:45

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0008_auto_20190817_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shope',
            name='bill',
            field=models.FileField(default='logo/default.png', upload_to='bill'),
        ),
        migrations.AlterField(
            model_name='shope',
            name='logo',
            field=models.FileField(default='logo/default.png', upload_to='logo', verbose_name=''),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('discription', models.TextField()),
                ('price', models.FloatField()),
                ('price_reduction', models.FloatField()),
                ('nb', models.IntegerField()),
                ('first_images', django.contrib.postgres.fields.ArrayField(base_field=models.FileField(upload_to=''), blank=True, null=True, size=5)),
                ('shope', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.Shope')),
            ],
        ),
    ]