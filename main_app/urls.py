from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('residences/', views.ResidenceList.as_view(),
         name='residences_index'),  # Residence routes
    path('workplaces/', views.WorkplaceList.as_view(),
         name='workplaces_index'),  # Workplace routes
]
