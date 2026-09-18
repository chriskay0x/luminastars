from django.urls import path
from . import views

app_name = 'membership'

urlpatterns = [
    path('', views.membership_page, name='page'),
    path('apply/<int:plan_id>/', views.apply, name='apply'),
    path('success/<int:application_id>/', views.success, name='success'),
]