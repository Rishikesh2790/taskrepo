
from django.urls import path,include
from shortner import views

urlpatterns = [
    path('createUI/', views.create,name='createUI'),
    path('list/', views.list,name='list'),
    path('createAPI/',views.createAPI,name='createAPI'),
    path('<str:token>/', views.display,name='display'),
    path('detail/<str:token>/', views.detail,name='detail'),
    path('delete/<str:token>/', views.delete,name='delete'),

]