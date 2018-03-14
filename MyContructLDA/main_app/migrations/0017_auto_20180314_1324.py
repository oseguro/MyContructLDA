# Generated by Django 2.0.2 on 2018-03-14 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0016_pedidoorcamento_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedidoorcamento',
            name='comprimento',
        ),
        migrations.RemoveField(
            model_name='pedidoorcamento',
            name='largura',
        ),
        migrations.AddField(
            model_name='pedidoorcamento',
            name='divisao',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.Divisao'),
            preserve_default=False,
        ),
    ]
