# Generated by Django 5.0.4 on 2024-04-26 01:18

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("socialmedia", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="post",
            options={"ordering": ["-created_at"]},
        ),
    ]
