from django.urls import path
from . import views

app_name = 'celebrities'

urlpatterns = [
    path('', views.celebrity_list, name='list'),
    path('<slug:slug>/', views.celebrity_detail, name='detail'),
]