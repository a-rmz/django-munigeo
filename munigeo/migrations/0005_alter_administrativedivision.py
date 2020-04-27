# Generated by Django 2.2.11 on 2020-04-24 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("munigeo", "0004_building"),
    ]

    operations = [
        migrations.AddField(
            model_name="administrativedivision",
            name="name_ar",
            field=models.CharField(db_index=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="administrativedivision",
            name="name_ru",
            field=models.CharField(db_index=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="administrativedivision",
            name="name_zh_hans",
            field=models.CharField(db_index=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="municipality",
            name="name_ar",
            field=models.CharField(db_index=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="municipality",
            name="name_ru",
            field=models.CharField(db_index=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="municipality",
            name="name_zh_hans",
            field=models.CharField(db_index=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="street",
            name="name_ar",
            field=models.CharField(db_index=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="street",
            name="name_ru",
            field=models.CharField(db_index=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="street",
            name="name_zh_hans",
            field=models.CharField(db_index=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="administrativedivision",
            name="level",
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name="administrativedivision",
            name="lft",
            field=models.PositiveIntegerField(editable=False),
        ),
        migrations.AlterField(
            model_name="administrativedivision",
            name="rght",
            field=models.PositiveIntegerField(editable=False),
        ),
    ]