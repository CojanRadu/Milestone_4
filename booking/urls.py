from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_booking, name='view_booking'),
    path('add/<property_id>/', views.add_booking, name='add_booking'),
]