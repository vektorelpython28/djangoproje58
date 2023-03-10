# Generated by Django 4.1.5 on 2023-02-04 08:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EsporModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=30, verbose_name='İsim')),
                ('nickname', models.CharField(max_length=20, verbose_name='Kullanıcı Adı')),
                ('mainhero', models.CharField(max_length=10, null=True, verbose_name='Oynanan Ana Ajan')),
                ('takim', models.CharField(max_length=30, verbose_name='Oynanan Takım')),
                ('giristarih', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
