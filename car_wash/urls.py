from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login_page),
    path('main/', views.m),
    path('import/', views.create_Import),
    path('ajustment/', views.create_ajustment),
    path('expense/', views.create_expense),
    path('service/', views.create_service),
    path('more_service/', views.more_service),
    path('save_service/', views.save_service),
    path('checkout_more_service/', views.checkout_moreservice),
    path('checkout/', views.checkout),
    path('checkout_new/', views.checkout_new),
    path('recipt/', views.recipt),
    path('print/', views.print),
    path('report_today/', views.report_today),
    path('report_date/', views.report_date)
]
