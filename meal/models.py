from django.db import models

# Create your models here.

from django.contrib.auth.models import User





class Meal2(models.Model):

    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="meals")

    

    MEAL_CHOICE=(
        ('Breakfast','Breakfast'),
        ('Lunch','Lunch'),
        ('Dinner','Dinner'),
        ('Snack','Snack'),
    )

    meal_type=models.CharField(max_length=100,choices=MEAL_CHOICE,default='Snack')

    calories=models.IntegerField()

    date=models.DateTimeField(auto_now_add=True)

    Name_of_meal=models.CharField(max_length=200)
