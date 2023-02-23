# Generated by Django 3.1.7 on 2021-04-12 16:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requested_date', models.DateField()),
                ('for_date', models.DateField()),
                ('district', models.CharField(max_length=254)),
                ('local_level', models.CharField(max_length=254)),
                ('blood_group', models.CharField(choices=[('pending', 'Pending'), ('verified', 'Verified'), ('completed', 'Completed')], max_length=10)),
                ('donated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='donated_by', to=settings.AUTH_USER_MODEL)),
                ('requested_by', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='requested_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]