# Generated by Django 4.0.5 on 2022-08-31 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blood_Camp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_camp', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=20)),
            ],
        ),
    ]