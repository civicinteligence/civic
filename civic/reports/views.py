from django.shortcuts import render
from intelligence.pipeline.nlp_struct import start
from .models import Report


def submit_report(request):
    msg = None
    if request.method == 'POST':
        message = request.POST.get('message', 'NA')
        place = request.POST.get('location', 'NA')
        coordinates = request.POST.get('coordinates', 'NA')
        
        try:
            # Save report to db
            report = Report.objects.create(
                message=message,
                location=place,
                gps=coordinates
            )
            # Start NLP pipeline
            if start(report):
                msg = 'Processed successfully.'
            else:
                msg = 'Report Not processed!'
            
        except Exception as e:
            msg = 'An Error Occured, please try again!'
            
    return render(request, 'reports.html', {'msg':msg})