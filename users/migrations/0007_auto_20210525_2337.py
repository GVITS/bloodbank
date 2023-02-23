# Generated by Django 3.1.7 on 2021-05-25 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20210525_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='blood_group',
            field=models.CharField(choices=[('AP', 'A+'), ('AN', 'A-'), ('BP', 'B+'), ('BN', 'B-'), ('ABP', 'AB+'), ('ABN', 'AB+'), ('OP', 'O+'), ('ON', 'O-')], max_length=3),
        ),
    ]