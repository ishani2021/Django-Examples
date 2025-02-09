# Generated by Django 5.0.7 on 2024-07-22 17:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="course",
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
                ("courseCode", models.CharField(max_length=10)),
                ("courseName", models.CharField(max_length=50)),
                ("courseCredits", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="student",
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
                ("usn", models.CharField(max_length=10)),
                ("name", models.CharField(max_length=40)),
                ("sem", models.IntegerField()),
                (
                    "courses",
                    models.ManyToManyField(
                        related_name="student_set", to="app4.course"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="projectReg",
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
                ("ptitle", models.CharField(max_length=30)),
                ("planguage", models.CharField(max_length=30)),
                ("pduration", models.IntegerField()),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app4.student"
                    ),
                ),
            ],
        ),
    ]
