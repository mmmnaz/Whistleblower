# Generated by Django 3.1.7 on 2021-04-17 02:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0015_delete_judgedetail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caseinfo',
            name='status',
            field=models.ForeignKey(default='Sagen er nyoprettet', on_delete=django.db.models.deletion.DO_NOTHING, related_name='status_name', to='case.status'),
        ),
    ]
