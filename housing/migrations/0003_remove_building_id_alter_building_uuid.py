# Generated by Django 4.0.2 on 2022-02-05 20:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('housing', '0002_alter_building_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='building',
            name='id',
        ),
        migrations.AlterField(
            model_name='building',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid1, primary_key=True, serialize=False),
        ),
    ]