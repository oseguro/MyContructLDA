# Generated by Django 2.0.2 on 2018-03-02 14:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0010_auto_20180302_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='projetos',
            name='categoria',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.Categoria'),
            preserve_default=False,
        ),
    ]