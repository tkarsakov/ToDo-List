# Generated by Django 4.2.2 on 2023-06-30 15:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("userauth", "0002_alter_user_username"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="password",
            field=models.CharField(max_length=50),
        ),
    ]
