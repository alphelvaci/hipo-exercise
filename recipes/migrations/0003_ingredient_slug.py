# Generated by Django 3.1.4 on 2020-12-31 10:58

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20201215_0322'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='name'),
        ),
    ]
