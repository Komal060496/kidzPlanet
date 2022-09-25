# Generated by Django 4.0.3 on 2022-03-28 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kidzapp', '0010_rename_organization_feedback_organization_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_message',
            name='user1_name',
        ),
        migrations.RemoveField(
            model_name='user_message',
            name='user2_name',
        ),
        migrations.AddField(
            model_name='user_message',
            name='receiver_id',
            field=models.CharField(default=None, max_length=45),
        ),
        migrations.AddField(
            model_name='user_message',
            name='receiver_status',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AddField(
            model_name='user_message',
            name='sender_id',
            field=models.CharField(default=None, max_length=45),
        ),
        migrations.AddField(
            model_name='user_message',
            name='sender_status',
            field=models.BooleanField(default=True, null=True),
        ),
    ]