# Generated by Django 2.1.4 on 2020-10-19 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Conta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titular', models.TextField()),
                ('numero', models.TextField()),
                ('saldo', models.FloatField()),
            ],
        ),
    ]
