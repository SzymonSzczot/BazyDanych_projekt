# Generated by Django 2.2.6 on 2019-12-15 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TyTube', '0003_auto_20191215_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='whenfaceappears',
            name='appeared_end',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='whenfaceappears',
            name='appeared_start',
            field=models.PositiveIntegerField(),
        ),
    ]