# Generated by Django 4.0.3 on 2022-03-25 09:00

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('kidzapp', '0009_rename_parentreg_parent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='organization',
            new_name='organization_name',
        ),
        migrations.AlterField(
            model_name='feedback',
            name='user_name',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='kidzapp.parent'),
        ),
        migrations.CreateModel(
            name='User_Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('user1_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='kidzapp.parent')),
                ('user2_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='kidzapp.organizer')),
            ],
        ),
    ]
