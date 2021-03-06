# Generated by Django 4.0.4 on 2022-05-25 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zavod', '0003_cliente'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cliente',
            options={'verbose_name': 'Cliente', 'verbose_name_plural': 'Todos los Clientes'},
        ),
        migrations.AlterField(
            model_name='cliente',
            name='email_cliente',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterUniqueTogether(
            name='cliente',
            unique_together={('rut_cliente',)},
        ),
    ]
