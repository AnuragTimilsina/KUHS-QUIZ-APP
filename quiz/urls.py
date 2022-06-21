from django.urls import path
from .views import *

urlpatterns = [
    path('category/', index_page, name='index_page'),
    path('category/<int:pk>/', take_quiz, name='take_quiz'),

]