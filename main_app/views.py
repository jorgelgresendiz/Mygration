from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Residence, Workplace


def home(request):
    return render(request, 'index.html')

# ---------------------- Residence Views -------------------------


class ResidenceList(ListView):
    model = Residence

# ---------------------- Workplace Views -------------------------


class WorkplaceList(ListView):
    model = Workplace
