# Generated by Django 5.0.4 on 2024-10-17 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_event_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='code',
            field=models.CharField(default=234567, max_length=10),
            preserve_default=False,
        ),
    ]
