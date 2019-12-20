from django.urls import path, include
from . import views

urlpatterns = [
    # Generic routes -----------------------------------
    path('', views.home, name='home'),
    path('select_entry_form/', views.select_entry_form, name='select_entry_form'),
    path('residences/create_form/', views.create_form, name='create_form'), # renders create form

    # Residence routes ---------------------------------
    path('residences/', views.residences_index,
         name='residences_index'),
    path('residences/<int:residence_id>/', views.residence_detail,
         name='residences_detail'),
    path('residences/create/', views.ResidenceCreate.as_view(), name='create_residence'),

    # Workplace routes ---------------------------------
    path('workplaces/', views.workplaces_index,
         name='workplaces_index'),
    path('workplaces/<int:workplace_id>/', views.workplace_detail,
         name='workplace_detail'),
    path('workplaces/create/', views.WorkplaceCreate.as_view(), name='create_workplace'),

    # Auth routes --------------------------------------
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
]
