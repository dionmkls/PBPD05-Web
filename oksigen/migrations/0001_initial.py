# Generated by Django 2.2.24 on 2021-10-28 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Oksigen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=30)),
                ('alamat', models.CharField(max_length=30)),
                ('telepon', models.CharField(max_length=30)),
            ],
        ),
    ]
