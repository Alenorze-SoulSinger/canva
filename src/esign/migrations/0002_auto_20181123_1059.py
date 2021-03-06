# Generated by Django 2.0.8 on 2018-11-23 10:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('esign', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SignForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('email', models.CharField(blank=True, max_length=256, null=True)),
                ('company', models.CharField(blank=True, max_length=256, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='signrequest',
            name='name',
        ),
        migrations.AddField(
            model_name='signrequest',
            name='agent',
            field=jsonfield.fields.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='signrequest',
            name='result',
            field=jsonfield.fields.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='signrequest',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='signform',
            name='sign_request',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='esign.SignRequest'),
        ),
    ]
