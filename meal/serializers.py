from rest_framework import serializers

from  django.contrib.auth.models import User

from meal.models import User,Meal2

class UsercreationSerializer(serializers.ModelSerializer):

    class Meta:

        model=User

        fields=["id","username","email","password"]

        read_ony_fields=["id"]

    def create(self, validated_data):

        return User.objects.create_user(**validated_data)
    


class MealSerializer(serializers.ModelSerializer):

    user=serializers.StringRelatedField(read_only=True)

    class Meta:

        model=Meal2

        fields="__all__"

        read_only_fields=["id","user","date"]