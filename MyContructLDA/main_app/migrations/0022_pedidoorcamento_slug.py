# Generated by Django 2.0.2 on 2018-04-10 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0021_auto_20180405_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedidoorcamento',
            name='slug',
            field=models.CharField(default='novo', max_length=100),
        ),
    ]
