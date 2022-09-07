# Generated by Django 4.1 on 2022-09-07 15:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("diklat", "0011_alter_diklatmodel_jabatan"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pesertamodel",
            name="nip",
            field=models.CharField(
                max_length=18,
                validators=[django.core.validators.MinLengthValidator(18)],
                verbose_name="Volume Number",
            ),
        ),
    ]
