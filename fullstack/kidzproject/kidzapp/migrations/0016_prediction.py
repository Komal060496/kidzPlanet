# Generated by Django 4.0.3 on 2022-05-02 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kidzapp', '0015_alter_feedback_user_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prediction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=45)),
                ('age', models.CharField(max_length=100)),
                ('gender', models.PositiveIntegerField(max_length=1)),
                ('interest', models.CharField(max_length=100)),
                ('playgroup', models.PositiveIntegerField(max_length=1)),
            ],
        ),
    ]
