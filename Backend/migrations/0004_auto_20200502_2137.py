# Generated by Django 3.0.5 on 2020-05-02 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0003_auto_20200429_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details_school',
            name='historique',
            field=models.TextField(blank=True, null=True),
        ),
    ]