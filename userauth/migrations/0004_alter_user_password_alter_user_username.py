# Generated by Django 4.2.2 on 2023-06-30 15:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("userauth", "0003_alter_user_password"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="password",
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.TextField(unique=True),
        ),
    ]
