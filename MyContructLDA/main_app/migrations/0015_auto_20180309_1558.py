# Generated by Django 2.0.2 on 2018-03-09 15:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0014_remove_pedidoorcamento_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='FotosProjeto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likes', models.IntegerField(default=0)),
                ('imagem', models.ImageField(default='media/default.png', upload_to='treasure_images')),
                ('projeto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Projetos')),
            ],
        ),
        migrations.AddField(
            model_name='pedidoorcamento',
            name='area',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pedidoorcamento',
            name='estilo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.Estilo'),
            preserve_default=False,
        ),
    ]
