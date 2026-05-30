from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from intelligence.models import Results
from django.db.models import F
from django.core.serializers.json import DjangoJSONEncoder
import json


@login_required
def dashboard(request):
    # This view returns only issues belonging to a user office
    office_issues = request.user.issue_category
    reports_qs = Results.objects.filter(category=office_issues)
    reports = list(reports_qs.values(
        "id",
        "category",
        "urgency",
        "location",
        "status",
        message= F("report__message"),
        time=F("report__time"),
        area=F("report__location"),
    ))

    data = {
        "reports": json.dumps(reports, cls=DjangoJSONEncoder),
        'office':office_issues.upper(),
        "total": reports_qs.count(),
        "high_urgency": Results.objects.filter(urgency='high', category=office_issues).count(),
        "low_urgency": Results.objects.filter(urgency='low', category=office_issues).count(),
        "resolved_issues": Results.objects.filter(status='resolved', category=office_issues).count(),
    }

    return render(request, 'dashboard.html', {"data": data})


@login_required
def all_issues(request):
    office = request.user.issue_category
    if office != 'general':
        return redirect('dashboard')

    reports_qs = Results.objects.all()
    reports = list(reports_qs.values(
        "id",
        "category",
        "urgency",
        "location",
        "status",
        message= F("report__message"),
        time=F("report__time"),
        area=F("report__location"),
    ))

    data = {
        "reports": json.dumps(reports, cls=DjangoJSONEncoder),
        "total": reports_qs.count(),
        "high_urgency": Results.objects.filter(urgency='high').count(),
        "low_urgency": Results.objects.filter(urgency='low').count(),
        "resolved_issues": Results.objects.filter(status='resolved').count(),
        "water_issues": Results.objects.filter(category='water').count(),
        "roads_issues": Results.objects.filter(category='roads').count(),
        "health_issues": Results.objects.filter(category='health').count(),
        "garbage_issues": Results.objects.filter(category='garbage').count(),
    }

    return render(request, 'all_issues.html', {"data": data})