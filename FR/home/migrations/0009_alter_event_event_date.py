# Generated by Django 5.0.4 on 2024-10-03 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_remove_picsrelation_pic_remove_picsrelation_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.DateField(),
        ),
    ]
