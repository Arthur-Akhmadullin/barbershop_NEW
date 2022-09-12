# Generated by Django 2.2.28 on 2022-09-12 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('barber_account', '0001_initial'),
        ('barber_orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='profile_orders', to='barber_account.Profile'),
        ),
    ]
