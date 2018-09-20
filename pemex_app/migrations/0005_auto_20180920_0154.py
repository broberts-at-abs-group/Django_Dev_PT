# Generated by Django 2.1 on 2018-09-20 01:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pemex_app', '0004_evidences'),
    ]

    operations = [
        migrations.AddField(
            model_name='documents',
            name='doc_comment_eng',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='documents',
            name='doc_comment_esp',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='documents',
            name='evidence',
            field=models.ForeignKey(blank=True, db_column='evidence', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='pemex_app.Evidences'),
        ),
        migrations.AddField(
            model_name='documents',
            name='evidence_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='documents',
            name='evidence_user',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='documents',
            name='installation',
            field=models.ForeignKey(blank=True, db_column='installation', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='pemex_app.Installations'),
        ),
        migrations.AddField(
            model_name='documents',
            name='trans_eng',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='documents',
            name='trans_esp',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]