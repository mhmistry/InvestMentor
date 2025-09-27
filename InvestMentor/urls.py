from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('investment/', views.investment, name='investment_planner'),
    path('broker/', views.broker, name='broker_tool'),
    path('roadmap/', views.roadmap_page, name='roadmap_page'),
    path('generate-roadmap/', views.generate_roadmap, name='generate_roadmap'),
]
