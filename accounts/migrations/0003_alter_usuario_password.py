# Generated by Django 4.2.16 on 2024-11-22 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_usuario_options_alter_usuario_managers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$600000$NYt6G2FvDjDkD7on0LvhV9$vLZpfg+qy0T4F1iCwLLgTjIztCFMZOQtzfRe9pArM6I=', max_length=128),
        ),
    ]
