# Generated by Django 4.2.16 on 2024-11-27 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0017_remove_mensagem_tipo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deck',
            name='n_cartoes',
        ),
        migrations.RemoveField(
            model_name='deck',
            name='n_dominados',
        ),
    ]
