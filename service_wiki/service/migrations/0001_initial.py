# Generated by Django 4.1.7 on 2023-02-15 20:09

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import service.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=256)),
            ],
            managers=[
                ('objects', service.managers.CategoryManager()),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('create_timestamp', models.DateTimeField()),
                ('timestamp', models.DateTimeField()),
                ('language', models.CharField(max_length=56)),
                ('wiki', models.CharField(max_length=256)),
                ('category', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=256), size=None)),
                ('title', models.CharField(max_length=256)),
                ('auxiliary_text', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=256), size=None)),
            ],
            managers=[
                ('objects', service.managers.ContentManager()),
            ],
        ),
        migrations.CreateModel(
            name='CategoryContent',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.category')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.content')),
            ],
            managers=[
                ('objects', service.managers.CategoryContentManager()),
            ],
        ),
    ]
