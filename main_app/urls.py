from django.urls import path, include
from . import views

urlpatterns = [
    # Generic routes -----------------------------------
    path('', views.home, name='home'),
    path('select_entry_form/', views.select_entry_form, name='select_entry_form'),
    path('residences/create_form/', views.create_form,
         name='create_form'),  # renders create form
    path('invalid_address/', views.invalid_address, name='invalid_address'),

    # Residence routes ---------------------------------
    path('residences/', views.residences_index,
         name='residences_index'),
    path('residences/<int:residence_id>/', views.residence_detail,
         name='residence_detail'),
    path('residences/create/', views.ResidenceCreate.as_view(),
         name='create_residence'),
    path('residences/<int:pk>/update/',
         views.ResidenceUpdate.as_view(), name='residence_update'),
    path('residences/<int:pk>/delete/',
         views.ResidenceDelete.as_view(), name='residence_delete'),

    # Workplace routes ---------------------------------
    path('workplaces/', views.workplaces_index,
         name='workplaces_index'),
    path('workplaces/<int:workplace_id>/', views.workplace_detail,
         name='workplace_detail'),
    path('workplaces/create/', views.WorkplaceCreate.as_view(),
         name='create_workplace'),
    path('workplaces/<int:pk>/update/',
         views.WorkplaceUpdate.as_view(), name='workplace_update'),
    path('workplaces/<int:pk>/delete/',
         views.WorkplaceDelete.as_view(), name='workplace_delete'),

    # Auth routes --------------------------------------
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
]
