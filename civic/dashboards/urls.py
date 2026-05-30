# Dashboards urls
from django.urls import path
from .views import dashboard, all_issues, update_issue_status

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('all', all_issues, name='all_issues'),
    path('update_status', update_issue_status, name='update_issue_status')
]
