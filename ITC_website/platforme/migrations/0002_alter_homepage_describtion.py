# Generated by Django 4.0.3 on 2022-04-29 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('platforme', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='describtion',
            field=models.TextField(blank=True),
        ),
    ]