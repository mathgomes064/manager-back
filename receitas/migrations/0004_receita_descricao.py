# Generated by Django 4.2.6 on 2023-10-13 18:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("receitas", "0003_alter_receita_owner"),
    ]

    operations = [
        migrations.AddField(
            model_name="receita",
            name="descricao",
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
    ]
