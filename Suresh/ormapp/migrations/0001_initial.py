# Generated by Django 5.0.2 on 2024-02-28 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Library_DB',
            fields=[
                ('serial', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20)),
                ('author', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
