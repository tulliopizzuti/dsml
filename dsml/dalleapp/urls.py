from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[

    path('',views.index, name='index'), 
    path('texts',views.texts,name='texts'),
    path('texts/api', views.TextListApiView.as_view()),
    path('texts/api/<int:id>', views.TextListApiView.as_view()),
    path('api/summary', views.SummaryApiView.as_view()),
    path('api/dalle', views.Dalle2ApiView.as_view()),
    path('wordtree',views.wordtree,name='wordtree'),
    path('settings/api', views.SettingsApiView.as_view())

]