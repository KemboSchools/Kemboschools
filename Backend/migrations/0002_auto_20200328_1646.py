# Generated by Django 3.0.3 on 2020-03-28 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myschoolrelationprofiluser',
            name='profil',
        ),
        migrations.RemoveField(
            model_name='myschoolrelationprofiluser',
            name='utilisateur',
        ),
        migrations.RenameField(
            model_name='myschoolmenu',
            old_name='app',
            new_name='myschoolapp',
        ),
        migrations.RenameField(
            model_name='myschoolsousmenu',
            old_name='menu',
            new_name='myschoolmenu',
        ),
        migrations.AddField(
            model_name='myschoolapp',
            name='myschoolprofil',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='MySchoolProfil_set', to='Backend.MySchoolUser'),
        ),
        migrations.AddField(
            model_name='myschoolprofil',
            name='myschool',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='MySchoolUser_set', to='Backend.MySchoolUser'),
        ),
        migrations.DeleteModel(
            name='MySchoolRelationAppProfil',
        ),
        migrations.DeleteModel(
            name='MySchoolRelationProfilUser',
        ),
    ]
