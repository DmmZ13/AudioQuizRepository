# Generated by Django 4.2.16 on 2024-11-23 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0028_alter_usuario_password_alter_usuario_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$600000$emMyC4ELKm357Z7xxNK7mh$RK3N+zD8j2IGT3KvTgXkH+M3bb8c2LLYV1nMlglqUbM=', max_length=128),
        ),
    ]