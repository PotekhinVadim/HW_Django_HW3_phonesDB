# Generated by Django 4.2.7 on 2023-11-06 09:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("phones", "0003_remove_phone_slug"),
    ]

    operations = [
        migrations.AddField(
            model_name="phone",
            name="slug",
            field=models.SlugField(default=None),
        ),
    ]