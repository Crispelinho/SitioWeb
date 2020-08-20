# Generated by Django 3.1b1 on 2020-08-07 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='correo',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='fotogragia',
            field=models.ImageField(null=True, upload_to='albums/images/'),
        ),
        migrations.AlterUniqueTogether(
            name='contacto',
            unique_together={('Ncelular',)},
        ),
    ]