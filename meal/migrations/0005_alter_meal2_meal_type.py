# Generated by Django 5.1.6 on 2025-03-04 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal', '0004_alter_meal2_meal_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal2',
            name='meal_type',
            field=models.CharField(choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner'), ('Snack', 'Snack')], default='Snack', max_length=100),
        ),
    ]
