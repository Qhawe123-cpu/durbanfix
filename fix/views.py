from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from .models import Report

def home(request):
    reports = Report.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'reports': reports})

def report_issue(request):
    if request.method == 'POST':
        issue = request.POST['issue']
        location = request.POST['location']
        description = request.POST['description']

        Report.objects.create(
            issue_type=issue,
            location=location,
            description=description
        )

        return redirect('home')

    return render(request, 'report.html')





def all_reports(request):
    from .models import Report
    reports = Report.objects.all()
    return render(request, 'all_reports.html', {'reports': reports})


def report_detail(request, id):
    from .models import Report
    report = Report.objects.get(id=id)
    return render(request, 'report_detail.html', {'report': report})