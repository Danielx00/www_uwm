from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('persons/', views.PersonsList.as_view()),
    path('persons/<int:pk>/', views.PersonsList.as_view()),
    path('teams/', views.DruzynaList.as_view()),
    path('teams/<int:pk>/', views.DruzynaDetail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)