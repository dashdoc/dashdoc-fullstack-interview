# Generated by Django 2.0 on 2017-12-05 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TruckGifs",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("url", models.URLField()),
                ("title", models.TextField(max_length=60)),
                ("height", models.PositiveSmallIntegerField()),
                ("width", models.PositiveSmallIntegerField()),
            ],
        )
    ]
