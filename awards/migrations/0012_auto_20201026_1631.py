# Generated by Django 3.1.2 on 2020-10-26 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0011_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='rater_profile', to='awards.profile'),
        ),
    ]