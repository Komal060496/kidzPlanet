# Generated by Django 4.0.3 on 2022-03-07 09:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=45)),
                ('phone', models.CharField(max_length=10)),
                ('your_query', models.TextField()),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]
