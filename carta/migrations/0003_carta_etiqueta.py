# Generated by Django 5.1.5 on 2025-02-06 08:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("carta", "0002_alter_carta_texto"),
    ]

    operations = [
        migrations.AddField(
            model_name="carta",
            name="etiqueta",
            field=models.CharField(
                choices=[
                    ("Nl", "No leido"),
                    ("Tra", "Tramitado"),
                    ("DA", "General"),
                    ("IgS", "Igualdad"),
                    ("AaE", "Estudiantes"),
                    ("Ca", "Calidad"),
                    ("Com", "Comunicacion"),
                ],
                default="No leido",
                max_length=100,
            ),
        ),
    ]
