# Generated by Django 4.0.3 on 2022-04-29 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='homePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagefile', models.FileField(null=True, upload_to='./static/images', verbose_name='')),
                ('describtion', models.CharField(max_length=255)),
            ],
        ),
    ]