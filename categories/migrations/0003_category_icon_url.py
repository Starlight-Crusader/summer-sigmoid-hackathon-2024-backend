# Generated by Django 4.2.13 on 2024-06-16 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='icon_url',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
