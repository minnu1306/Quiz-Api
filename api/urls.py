from django.urls import path
from .views import QuesL,ChoiceL,Result

urlpatterns = [
   
    path('quiz/',QuesL.as_view()),
    path('quiz/<int:id>/',ChoiceL.as_view()),
    path('result/',Result.as_view()),
   
]
