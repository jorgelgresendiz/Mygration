from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('residences/', views.ResidenceList.as_view(),
         name='residences_index'),  # Residence routes
    path('residences/<residence_id/', views.ResidenceDetail.as_view(),
         name='residences_detail'),
    path('residences/create/', views.create_residence, name='create_residence'),
    path('workplaces/', views.WorkplaceList.as_view(),
         name='workplaces_index'),  # Workplace routes
    path('workplaces/<workplace_id>/', views.WorkplaceDetail.as_view(),
         name='workplaces_detail'),
    path('workplaces/create/', views.create_workplace, name='create_workplace'),
]
