# Generated by Django 4.0.2 on 2022-10-18 00:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0004_alter_player_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='guild',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='db.guild'),
        ),
    ]