# Generated by Django 4.1.4 on 2023-10-09 21:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("shops", "0006_post_ciudad_id_alter_post_ciudad"),
    ]

    operations = [
        migrations.CreateModel(
            name="Country",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name_country", models.CharField(max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name="post",
            name="pais",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="shops.country",
            ),
        ),
    ]
