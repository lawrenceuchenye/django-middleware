# Generated by Django 4.1.3 on 2023-06-13 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserStat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('android', models.IntegerField()),
                ('desktop', models.IntegerField()),
            ],
        ),
    ]