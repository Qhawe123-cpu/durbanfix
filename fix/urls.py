from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('report/', views.report_issue, name='report'),

    path('reports/', views.all_reports, name='all_reports'),
    path('report/<int:id>/', views.report_detail, name='report_detail'),
]