# Generated by Django 5.0.7 on 2024-07-24 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=120)),
                ('description', models.CharField(max_length=300)),
            ],
        ),
    ]
