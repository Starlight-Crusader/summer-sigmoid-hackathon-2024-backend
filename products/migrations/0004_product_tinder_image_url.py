# Generated by Django 4.2.13 on 2024-06-16 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tinder_image_url',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
