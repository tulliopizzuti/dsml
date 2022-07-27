from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[

    path('',views.index), 
    path('texts',views.texts,name='texts'),
    path('texts/api', views.TextListApiView.as_view()),
    path('texts/api/<int:id>', views.TextListApiView.as_view()),
    path('wordtree',views.wordtree,name='wordtree'),

]