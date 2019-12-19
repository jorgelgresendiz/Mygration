from django.urls import path, include
from . import views

urlpatterns = [
    # Generic routes -----------------------------------
    path('', views.home, name='home'),

    # Residence routes ---------------------------------
    path('residences/', views.residences_index,
         name='residences_index'),
    path('residences/<int:residence_id>/', views.residence_detail,
         name='residences_detail'),
    path('residences/create/', views.create_residence, name='create_residence'),

    # Workplace routes ---------------------------------
    path('workplaces/', views.workplaces_index,
         name='workplaces_index'),
    path('workplaces/<int:workplace_id>/', views.workplace_detail,
         name='workplace_detail'),
    path('workplaces/create/', views.create_workplace, name='create_workplace'),

    # Auth routes --------------------------------------
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
]
