# Generated by Django 5.1.5 on 2025-02-06 09:12

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("carta", "0005_alter_carta_etiqueta"),
    ]

    operations = [
        migrations.AddField(
            model_name="carta",
            name="fecha",
            field=models.DateField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
