# Generated by Django 4.1 on 2022-09-07 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("reports", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="iocs",
            name="cve",
            field=models.TextField(default="No information", max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="iocs",
            name="domain",
            field=models.TextField(default="No information", max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="iocs",
            name="email",
            field=models.TextField(default="No information", max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="iocs",
            name="ip",
            field=models.TextField(default="No information", max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="iocs",
            name="md5",
            field=models.TextField(default="No information", max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="iocs",
            name="sha1",
            field=models.TextField(default="No information", max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="iocs",
            name="sha256",
            field=models.TextField(default="No information", max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="iocs",
            name="url",
            field=models.TextField(default="No information", max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="report",
            name="iocs",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="iocs",
                to="reports.iocs",
            ),
        ),
    ]
