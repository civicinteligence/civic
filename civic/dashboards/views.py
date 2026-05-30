from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db import transaction
from intelligence.models import Results
from django.db.models import F
from django.core.serializers.json import DjangoJSONEncoder
import json


@login_required
def dashboard(request):
    # This view returns only issues belonging to a user office
    office_issues = request.user.issue_category
    reports_qs = Results.objects.filter(category=office_issues, status='pending')
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
        "high_urgency": Results.objects.filter(urgency='high', status='pending',  category=office_issues).count(),
        "low_urgency": Results.objects.filter(urgency='low', status='pending',  category=office_issues).count(),
        "resolved_issues": Results.objects.filter(status='resolved', category=office_issues).count(),
    }

    return render(request, 'dashboard.html', {"data": data})


@login_required
def all_issues(request):
    office = request.user.issue_category
    if office != 'general':
        return redirect('dashboard')

    reports_qs = Results.objects.filter(status='pending')
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
        'office':office.upper(),
        "total": reports_qs.count(),
        "high_urgency": Results.objects.filter(urgency='high', status='pending').count(),
        "low_urgency": Results.objects.filter(urgency='low', status='pending').count(),
        "resolved_issues": Results.objects.filter(status='resolved').count(),
        "water_issues": Results.objects.filter(category='water', status='pending').count(),
        "roads_issues": Results.objects.filter(category='roads', status='pending').count(),
        "health_issues": Results.objects.filter(category='health', status='pending').count(),
        "garbage_issues": Results.objects.filter(category='garbage', status='pending').count(),
    }

    return render(request, 'all_issues.html', {"data": data})


@login_required
def update_issue_status(request):
    if request.method == 'POST':
        #issue_id = request.POST.get('issue_id')
        location = request.POST.get('location')
        category = request.POST.get('category')
        status = request.POST.get('status')
        
        place = Results.objects.filter(location=location).first().report.location
        
        with transaction.atomic():
            reports = Results.objects.select_for_update().filter(report__location=place, category=category)
            for report in reports:
                report.status = status
                report.save()
        return redirect("all_issues")
    return redirect("all_issues")