# Generated by Django 5.1.6 on 2025-03-11 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("events", "0002_alter_users_options_alter_users_managers_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="users",
            name="email",
            field=models.EmailField(max_length=254, unique=True, verbose_name="email"),
        ),
    ]
