from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('persons/', views.person_list),
    path('persons/<int:pk>/', views.person_detail),
    path('persons/delete/<int:pk>/', views.person_update_delete),
    path('persons/update/<int:pk>/', views.person_update_delete),
    path('teams/', views.team_list),
    path('teams/<int:pk>/', views.team_detail),
    path('persons/permcheck/<int:pk>/', views.person_view, name='person_view'),

]