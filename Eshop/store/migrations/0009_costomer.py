# Generated by Django 3.1.3 on 2020-11-17 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_delete_costomer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Costomer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone_no', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=500)),
            ],
        ),
    ]
