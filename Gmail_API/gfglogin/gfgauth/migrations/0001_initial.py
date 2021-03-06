# Generated by Django 3.1 on 2020-08-26 06:43

from django.db import migrations, models
import django.db.models.deletion
import oauth2client.contrib.django_util.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CredentialsModel',
            fields=[
                ('id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('credential', oauth2client.contrib.django_util.models.CredentialsField(null=True)),
                ('task', models.CharField(max_length=80, null=True)),
                ('updated_time', models.CharField(max_length=80, null=True)),
            ],
        ),
    ]
