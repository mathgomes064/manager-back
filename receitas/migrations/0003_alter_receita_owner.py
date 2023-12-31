# Generated by Django 4.2.6 on 2023-10-09 22:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("receitas", "0002_receita_owner"),
    ]

    operations = [
        migrations.AlterField(
            model_name="receita",
            name="owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="receitas",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
