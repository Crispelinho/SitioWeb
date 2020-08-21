# Generated by Django 3.1b1 on 2020-08-20 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestioncontactos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('color', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('type', models.IntegerField(choices=[(1, 'Sedan'), (2, 'Truck'), (4, 'SUV')])),
            ],
        ),
        migrations.RenameField(
            model_name='contacto',
            old_name='fotogragia',
            new_name='fotografia',
        ),
    ]