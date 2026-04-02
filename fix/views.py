from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Report

def home(request):
    reports = Report.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'reports': reports})

def report_issue(request):
    if request.method == 'POST':
        issue_type = request.POST.get('issue_type')
        location = request.POST.get('location')
        description = request.POST.get('description')

        if issue_type and location and description:
            Report.objects.create(
                issue_type=issue_type,
                location=location,
                description=description
            )
            messages.success(request, "✅ Issue reported successfully!")
            return redirect('home')
        else:
            messages.error(request, "❌ Please fill in all fields.")

    return render(request, 'report.html')