# Generated by Django 4.1 on 2022-09-05 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("diklat", "0004_rename_asal_instansi_pesertamodel_instansi"),
    ]

    operations = [
        migrations.AddField(
            model_name="pesertamodel",
            name="jabatan",
            field=models.CharField(max_length=30, null=True),
        ),
    ]
