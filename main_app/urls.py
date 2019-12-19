from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'), # Generic routes
    path('residences/', views.residences_index,
         name='residences_index'),  # Residence routes

    path('residences/<residence_id/', views.ResidenceDetail.as_view(),
         name='residences_detail'),
    path('residences/create/', views.create_residence, name='create_residence'),
    path('workplaces/', views.WorkplaceList.as_view(),
         name='workplaces_index'),  # Workplace routes
    path('workplaces/<workplace_id>/', views.WorkplaceDetail.as_view(),
         name='workplaces_detail'),
    path('workplaces/create/', views.create_workplace, name='create_workplace'),
    path('residences/<int:residence_id/', views.residence_detail,
         name='residence_detail'),
    path('residences/create/', views.create_residence, name='create_residence'),
    path('workplaces/', views.workplaces_index,
         name='workplaces_index'),  # Workplace routes
    path('workplaces/<int:workplace_id>/', views.workplace_detail,
         name='workplace_detail'),
    path('workplaces/create/', views.create_workplace, name='create_workplace'),
    path('accounts/', include('django.contrib.auth.urls')), # Auth routes
	path('accounts/signup/', views.signup, name='signup'),
]
