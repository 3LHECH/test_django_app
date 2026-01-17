
from django.contrib import admin
from django.urls import path,include
from .views import game,save_score
urlpatterns = [
    path('', game, name="block-game"),
    path('save-score/', save_score, name="save-score"),

]
