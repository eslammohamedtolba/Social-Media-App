# Generated by Django 5.0.4 on 2024-04-28 13:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("socialmedia", "0016_remove_post_likes_post_likes"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="likes",
            field=models.ManyToManyField(
                null=True, related_name="liked_posts", to="socialmedia.userprofile"
            ),
        ),
    ]
