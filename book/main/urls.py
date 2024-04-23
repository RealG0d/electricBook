from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lection_1/', views.lection_1, name='lection_1'),
    path('lection_2/', views.lection_2, name='lection_2'),
    path('lection_3/', views.lection_3, name='lection_3'),
    path('lection_4/', views.lection_4, name='lection_4'),
    path('lection_5/', views.lection_5, name='lection_5'),
    path('lection_6/', views.lection_6, name='lection_6'),
    path('practice_1/', views.practice_1, name='practice_1'),
    path('practice_2/', views.practice_2, name='practice_2'),
    path('practice_3/', views.practice_3, name='practice_3'),
    path('practice_4/', views.practice_4, name='practice_4'),
    path('last_test/', views.last_test, name='last_test'),
]
