# Generated by Django 3.1.3 on 2020-11-15 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20201109_1200'),
    ]

    operations = [
        migrations.CreateModel(
            name='Costomer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phoneno', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=500)),
            ],
        ),
    ]