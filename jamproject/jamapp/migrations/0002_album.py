# Generated by Django 4.1.3 on 2022-11-17 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jamapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25, unique=True)),
                ('release_date', models.DateField()),
            ],
        ),
    ]
