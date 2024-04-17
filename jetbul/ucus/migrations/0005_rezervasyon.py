# Generated by Django 5.0.4 on 2024-04-17 18:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ucus", "0004_alter_rota_options_rotaplan"),
    ]

    operations = [
        migrations.CreateModel(
            name="Rezervasyon",
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
                ("ucus_saati", models.TimeField()),
                ("isim", models.CharField(max_length=120)),
                ("soyisim", models.CharField(max_length=120)),
                ("tc", models.CharField(max_length=11)),
                (
                    "rotaplan",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="RotaPlan",
                        to="ucus.rotaplan",
                    ),
                ),
            ],
            options={
                "verbose_name": "Rezervasyon",
                "verbose_name_plural": "Rezervasyonlar",
            },
        ),
    ]
