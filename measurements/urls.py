from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.get_measurements, name='measurementList'),
    path('<str:id>/', views.get_measurement_id, name='measurementId'),
    path('delete/<str:id>/', views.delete_measurement_id, name='deleteMeasurement'),
]