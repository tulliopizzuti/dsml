from django.urls import path
from . import views

urlpatterns=[

    path('',views.index),
    path('texts',views.texts,name='texts'),
    path('wordtree',views.wordtree,name='wordtree'),

]