# Generated by Django 5.0.4 on 2024-04-26 22:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("socialmedia", "0011_alter_userprofile_backgroundimage"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="backgroundImage",
            field=models.ImageField(blank=True, null=True, upload_to="profile_images/"),
        ),
    ]