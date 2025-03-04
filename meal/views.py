from django.shortcuts import render,get_object_or_404

# Create your views here.

from meal.serializers import UsercreationSerializer,MealSerializer

from rest_framework.generics import CreateAPIView,ListAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView

from meal.models import Meal2

from rest_framework import authentication,permissions

from django.db.models import Sum

from rest_framework.response import Response

from meal.permissions import IsOwnerPermissionRequired

class UserCreationView(CreateAPIView):

    serializer_class=UsercreationSerializer

class MealAddView(CreateAPIView,ListAPIView):

    authentication_classes=[authentication.BasicAuthentication]

    permission_classes=[permissions.IsAuthenticated]

    serializer_class=MealSerializer

    queryset=Meal2.objects.all()

    def perform_create(self, serializer):

        return serializer.save(user=self.request.user)
    
class MealRetriveUpdateDestroyView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):

    authentication_classes=[authentication.BasicAuthentication]

    permission_classes=[IsOwnerPermissionRequired]


    serializer_class=MealSerializer

    queryset=Meal2.objects.all()

    
class MealRetriveTotalCalorieView(RetrieveAPIView):

    authentication_classes=[authentication.BasicAuthentication]

    permission_classes=[IsOwnerPermissionRequired]


    serializer_class=MealSerializer

    queryset=Meal2.objects.all()

    def get(self,request,*args,**kwargs):

        calorie_total=Meal2.objects.filter(user=request.user).values("calories").aggregate(total=Sum("calories"))

        context={
            "calorie_total=":calorie_total.get("total"),
            
        }
        return Response(data=context)
    

class MealTypeAndDateView(RetrieveAPIView):

    authentication_classes=[authentication.BasicAuthentication]

    permission_classes=[IsOwnerPermissionRequired]

    serializer_class=MealSerializer

    def get(self,request,*args,**kwargs):

        date_and_meal_type=Meal2.objects.filter(user=request.user).values("date","meal_type")

        return Response(data=date_and_meal_type)
        


# class MealCalorieIntake(RetrieveAPIView):

#     authentication_classes=[authentication.BasicAuthentication]

#     permission_classes=[IsOwnerPermissionRequired]

#     serializer_class=MealSerializer

#     def get(self,request,*args,**kwargs):

#         calorie_intake=Meal2.objects.filter(user=request.user).values('meal_type').annotate(total_calories=Sum('calories'))

#         return Response(data=calorie_intake)


