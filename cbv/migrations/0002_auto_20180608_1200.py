# Generated by Django 2.0.5 on 2018-06-08 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cbv', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='family',
            name='last_name',
            field=models.CharField(choices=[('Dube', 'Dube'), ('Mabuto', 'Mabuto'), ('Kubiku', 'Kubiku')], max_length=10),
        ),
    ]