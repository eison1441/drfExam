from django.urls import path

from meal import views


urlpatterns=[

    path("user/",views.UserCreationView.as_view()),
    path('mealadd/',views.MealAddView.as_view()),
    path("meals/<int:pk>/",views.MealRetriveUpdateDestroyView.as_view()),
    path("mealtotalcalorie/<int:pk>/",views.MealRetriveTotalCalorieView.as_view()),
    path("date/mealtype/",views.MealTypeAndDateView.as_view()),


]