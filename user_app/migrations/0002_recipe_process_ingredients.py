# Generated by Django 4.1.5 on 2023-01-12 17:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('recipe_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('desc', models.CharField(max_length=500)),
                ('image_url', models.ImageField(upload_to='food_recipe')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipe', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Process',
            fields=[
                ('process_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('step', models.CharField(max_length=500)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='process', to='user_app.recipe')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('ingredient_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('items', models.CharField(max_length=50)),
                ('amount', models.IntegerField()),
                ('unit', models.CharField(max_length=50)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredient', to='user_app.recipe')),
            ],
        ),
    ]
