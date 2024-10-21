# Generated by Django 5.1.2 on 2024-10-20 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_userid', models.CharField(max_length=50, unique=True)),
                ('user_password', models.CharField(max_length=255)),
                ('user_email', models.EmailField(max_length=100, unique=True)),
                ('user_name', models.CharField(max_length=255)),
                ('user_address', models.CharField(max_length=255)),
                ('user_phoneNum', models.CharField(max_length=11)),
                ('user_created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
