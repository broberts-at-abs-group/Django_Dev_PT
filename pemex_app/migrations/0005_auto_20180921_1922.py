# Generated by Django 2.1 on 2018-09-21 19:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pemex_app', '0004_fieldinputs_input_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fieldinputs',
            name='input_user',
            field=models.ForeignKey(blank=True, db_column='input_user', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='items',
            name='next_responsible',
            field=models.ForeignKey(blank=True, db_column='next_reponsible', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]