# Generated by Django 3.2.8 on 2021-10-07 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_from', models.EmailField(max_length=250)),
                ('subject', models.CharField(max_length=300)),
                ('message', models.TextField()),
            ],
        ),
    ]
