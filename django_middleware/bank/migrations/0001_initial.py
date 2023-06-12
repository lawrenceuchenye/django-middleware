# Generated by Django 4.1.3 on 2023-06-12 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('e_signature', models.CharField(blank=True, max_length=255, null=True)),
                ('pin', models.IntegerField()),
                ('balance', models.DecimalField(decimal_places=100, default=1000, max_digits=100)),
                ('basic_info', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ETranzact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_creditor', models.CharField(max_length=255)),
                ('to_creditee', models.CharField(max_length=255)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=100)),
            ],
        ),
    ]
