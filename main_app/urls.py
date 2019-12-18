from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('residences/', views.ResidenceList.as_view(),
         name='residences_index'),  # Residence routes
    path('residences/<int:pk>/', views.ResidenceDetail.as_view(),
         name='residences_detail'),
    path('workplaces/', views.WorkplaceList.as_view(),
         name='workplaces_index'),  # Workplace routes
    path('workplaces/<int:pk>/', views.WorkplaceDetail.as_view(),
         name='workplaces_detail'),
]
