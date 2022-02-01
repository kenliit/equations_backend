from django.urls import path
from .views import check_connection, get_question, check_answer

urlpatterns = [
    path('check_connection/', check_connection, name='check_connection'),
    path('get_question/', get_question, name='get_question'),
    path("check_answer/", check_answer, name='check_answer'),
]
