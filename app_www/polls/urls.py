from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('persons/', views.PersonsList.as_view()),
    path('persons/<int:pk>/', views.PersonsList.as_view()),
    path('teams/', views.team_list),
    path('teams/<int:pk>/', views.team_detail),

]

urlpatterns = format_suffix_patterns(urlpatterns)