# Generated by Django 2.2 on 2019-04-21 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0003_auto_20190421_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='statments',
            field=models.TextField(),
        ),
    ]