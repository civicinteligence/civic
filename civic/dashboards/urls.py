# Dashboards urls
from django.urls import path
from .views import dashboard, all_issues

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('all', all_issues, name='all_issues'),
]
