from django.urls import path
from . import views

urlpatterns = [
    path('alerts/', views.budget_alerts, name='budget_alerts'),
    path('alerts/delete/<int:alert_id>/', views.delete_alert, name='delete_alert'),
]
