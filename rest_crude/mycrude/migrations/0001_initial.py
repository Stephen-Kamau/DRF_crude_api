# Generated by Django 3.0.7 on 2020-07-31 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mycrude',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('published', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'Mycrude',
            },
        ),
    ]
