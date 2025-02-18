# Generated by Django 5.1.6 on 2025-02-16 00:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pacientes", "0007_consultas_created_at_consultas_updated_at"),
    ]

    operations = [
        migrations.CreateModel(
            name="Visualizacoes",
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
                ("ip", models.GenericIPAddressField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "consulta",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="pacientes.consultas",
                    ),
                ),
            ],
        ),
    ]
