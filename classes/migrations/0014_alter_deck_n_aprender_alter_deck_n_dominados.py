# Generated by Django 5.1.1 on 2024-11-23 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0013_alter_arquivo_classe_alter_mensagem_classe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deck',
            name='n_aprender',
            field=models.IntegerField(default=models.IntegerField()),
        ),
        migrations.AlterField(
            model_name='deck',
            name='n_dominados',
            field=models.IntegerField(default=0),
        ),
    ]
