# Generated by Django 2.2 on 2020-06-09 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_page_thumb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='thumb',
            field=models.ImageField(blank=True, default='default_2.png', upload_to=''),
        ),
    ]
