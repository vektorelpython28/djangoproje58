# Generated by Django 4.1.5 on 2023-01-29 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ediz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ornekdata',
            name='adres',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ornekdata',
            name='kayitzaman',
            field=models.DateTimeField(null=True),
        ),
    ]
