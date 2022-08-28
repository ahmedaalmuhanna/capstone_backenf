# Generated by Django 4.1 on 2022-08-28 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("reports", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="iocs",
            name="cve",
            field=models.TextField(default="", max_length=255),
        ),
        migrations.AddField(
            model_name="iocs",
            name="domain",
            field=models.TextField(default="", max_length=255),
        ),
        migrations.AddField(
            model_name="iocs",
            name="email",
            field=models.TextField(default="", max_length=255),
        ),
        migrations.AddField(
            model_name="iocs",
            name="ip",
            field=models.TextField(default="", max_length=255),
        ),
        migrations.AddField(
            model_name="iocs",
            name="md5",
            field=models.TextField(default="", max_length=255),
        ),
        migrations.AddField(
            model_name="iocs",
            name="sha1",
            field=models.TextField(default="", max_length=255),
        ),
        migrations.AddField(
            model_name="iocs",
            name="sha256",
            field=models.TextField(default="", max_length=255),
        ),
        migrations.AddField(
            model_name="iocs",
            name="url",
            field=models.TextField(default="", max_length=255),
        ),
        migrations.AddField(
            model_name="report",
            name="details",
            field=models.TextField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="report",
            name="iocs",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.DO_NOTHING,
                related_name="iocs",
                to="reports.iocs",
            ),
        ),
        migrations.AddField(
            model_name="report",
            name="reference",
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name="report",
            name="title",
            field=models.CharField(max_length=200, null=True),
        ),
    ]
