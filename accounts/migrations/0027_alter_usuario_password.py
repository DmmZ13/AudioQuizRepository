# Generated by Django 4.2.16 on 2024-11-23 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0026_alter_usuario_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$600000$1PcFpIqTl0OlS3iwpTgTeF$yIbW/St82sycBVDqjSc7sgCPnfgzY2HPfBc3ci2Qz/w=', max_length=128),
        ),
    ]
