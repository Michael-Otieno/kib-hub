# Generated by Django 4.1.4 on 2022-12-29 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kibhub', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='contacts',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='property',
            name='category',
            field=models.CharField(choices=[('house', 'house'), ('office', 'office'), ('shop', 'shop'), ('kibanda', 'kibanda')], default=('office', 'office'), max_length=200),
        ),
    ]