# Generated by Django 4.2.16 on 2024-11-23 05:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0012_alter_arquivo_classe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arquivo',
            name='classe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.classe'),
        ),
        migrations.AlterField(
            model_name='mensagem',
            name='classe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mensagens', to='classes.classe'),
        ),
    ]
