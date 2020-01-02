from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.core import serializers
from .models import Residence, Workplace
import os
import requests
import json


# ---------------------- Generic Views ---------------------------

def home(request):
    if request.user.is_authenticated:
        residences = serializers.serialize(
            "json", Residence.objects.filter(user=request.user).order_by('end_date'))
        test_data = json.loads(residences)
        return render(request, 'index.html', {'residences': test_data, 'DIRECTIONS_KEY': os.environ['DIRECTIONS_KEY']})
    else:
        return render(request, 'index.html')


def create_form(request):
    return render(request, 'create_residences.html')


def select_entry_form(request):
    return render(request, 'select.html')


def invalid_address(request):
    return render(request, 'invalid_address.html')

# ---------------------- Residence Views -------------------------


@login_required
def residences_index(request):
    residence = Residence.objects.filter(
        user=request.user).order_by('-end_date')
    return render(request, 'residences/residences_index.html', {'residences': residence})


@login_required
def residence_detail(request, residence_id):
    residence = Residence.objects.get(id=residence_id)
    return render(request, 'residences/residence_detail.html', {
        'residence': residence})


class ResidenceCreate(LoginRequiredMixin, CreateView):
    model = Residence
    fields = ['address_line_1', 'address_line_2',
              'city', 'state', 'start_date', 'end_date']
    success_url = '/residences/'

    def build_static_map_url(self, lat, long, key):
        url = f'https://maps.googleapis.com/maps/api/staticmap?center={lat},{long}&zoom=13&size=600x300&maptype=roadmap&markers=color:purple%7Clabel:%7C{lat},{long}&key={key}'
        return url

    def build_static_streetview_url(self, lat, long, key):
        url = f'https://maps.googleapis.com/maps/api/streetview?size=600x300&location={lat},{long}&heading=&pitch=0&key={key}'
        return url

    def form_valid(self, form):
        form.instance.user = self.request.user
        street_1 = form.instance.address_line_1
        street_1_formatted = street_1.replace(' ', '%20')
        street_2 = form.instance.address_line_2
        start_date = form.instance.start_date
        end_date = form.instance.end_date
        city = form.instance.city
        state = form.instance.state
        request_string = f"https://us-street.api.smartystreets.com/street-address?auth-id={os.environ['SS_AUTH_ID']}&auth-token={os.environ['SS_AUTH_TOKEN']}&street={street_1_formatted}&street2=&city={city}&state={state}&zipcode=&address-type=us-street-components"
        unparsed_formatted_address = requests.get(request_string)
        parsed_formatted_address = json.loads(
            unparsed_formatted_address.content)
        if len(parsed_formatted_address) < 1:
            print('invalid address')
            return redirect('invalid_address')
        form.instance.address_line_1 = parsed_formatted_address[0]['delivery_line_1']
        form.instance.address_line_2 = street_2
        form.instance.city = parsed_formatted_address[0]['components']['city_name']
        form.instance.state = parsed_formatted_address[0]['components']['state_abbreviation']
        form.instance.zipcode = parsed_formatted_address[0]['components']['zipcode']
        form.instance.latitude = parsed_formatted_address[0]['metadata']['latitude']
        form.instance.longitude = parsed_formatted_address[0]['metadata']['longitude']
        form.instance.start_date = start_date
        form.instance.end_date = end_date
        form.instance.static_map_url = self.build_static_map_url(
            form.instance.latitude, form.instance.longitude, os.environ['STATIC_MAPS_KEY'])
        form.instance.static_streetview_url = self.build_static_streetview_url(
            form.instance.latitude, form.instance.longitude, os.environ['STREETVIEW_KEY'])
        print(form.instance.static_map_url)
        print(form.instance.static_streetview_url)
        if 'addnew' in form.data:
            self.success_url = '/select_entry_form/'
            return super().form_valid(form)
        elif 'detail' in form.data:
            return super().form_valid(form)


class ResidenceUpdate(LoginRequiredMixin, UpdateView):
    model = Residence
    fields = ['address_line_1', 'address_line_2',
              'city', 'state', 'start_date', 'end_date']

    def build_static_map_url(self, lat, long, key):
        url = f'https://maps.googleapis.com/maps/api/staticmap?center={lat},{long}&zoom=13&size=600x300&maptype=roadmap&markers=color:purple%7Clabel:%7C{lat},{long}&key={key}'
        return url

    def build_static_streetview_url(self, lat, long, key):
        url = f'https://maps.googleapis.com/maps/api/streetview?size=600x300&location={lat},{long}&heading=&pitch=0&key={key}'
        return url

    def form_valid(self, form):
        form.instance.user = self.request.user
        street_1 = form.instance.address_line_1
        street_1_formatted = street_1.replace(' ', '%20')
        street_2 = form.instance.address_line_2
        start_date = form.instance.start_date
        end_date = form.instance.end_date
        city = form.instance.city
        state = form.instance.state
        request_string = f"https://us-street.api.smartystreets.com/street-address?auth-id={os.environ['SS_AUTH_ID']}&auth-token={os.environ['SS_AUTH_TOKEN']}&street={street_1_formatted}&street2=&city={city}&state={state}&zipcode=&address-type=us-street-components"
        unparsed_formatted_address = requests.get(request_string)
        parsed_formatted_address = json.loads(
            unparsed_formatted_address.content)
        if len(parsed_formatted_address) < 1:
            print('invalid address')
            return redirect('invalid_address')
        form.instance.address_line_1 = parsed_formatted_address[0]['delivery_line_1']
        form.instance.address_line_2 = street_2
        form.instance.city = parsed_formatted_address[0]['components']['city_name']
        form.instance.state = parsed_formatted_address[0]['components']['state_abbreviation']
        form.instance.zipcode = parsed_formatted_address[0]['components']['zipcode']
        form.instance.latitude = parsed_formatted_address[0]['metadata']['latitude']
        form.instance.longitude = parsed_formatted_address[0]['metadata']['longitude']
        form.instance.start_date = start_date
        form.instance.end_date = end_date
        form.instance.static_map_url = self.build_static_map_url(
            form.instance.latitude, form.instance.longitude, os.environ['STATIC_MAPS_KEY'])
        form.instance.static_streetview_url = self.build_static_streetview_url(
            form.instance.latitude, form.instance.longitude, os.environ['STREETVIEW_KEY'])
        return super().form_valid(form)


class ResidenceDelete(LoginRequiredMixin, DeleteView):
    model = Residence
    success_url = '/residences/'


# ---------------------- Workplace Views -------------------------

@login_required
def workplaces_index(request):
    workplace = Workplace.objects.filter(
        user=request.user).order_by('-end_date')
    return render(request, 'workplaces/workplaces_index.html', {'workplaces': workplace})


@login_required
def workplace_detail(request, workplace_id):
    workplace = Workplace.objects.get(id=workplace_id)
    return render(request, 'workplaces/workplace_detail.html', {
        'workplace': workplace})


class WorkplaceCreate(LoginRequiredMixin, CreateView):
    model = Workplace
    fields = ['address_line_1', 'address_line_2', 'city', 'state', 'start_date', 'end_date',
              'company_name', 'employer_name', 'employer_number', 'employer_email', 'title']
    success_url = '/workplaces/'

    def build_static_map_url(self, lat, long, key):
        url = f'https://maps.googleapis.com/maps/api/staticmap?center={lat},{long}&zoom=13&size=600x300&maptype=roadmap&markers=color:purple%7Clabel:%7C{lat},{long}&key={key}'
        return url

    def build_static_streetview_url(self, lat, long, key):
        url = f'https://maps.googleapis.com/maps/api/streetview?size=600x300&location={lat},{long}&heading=&pitch=0&key={key}'
        return url

    def form_valid(self, form):
        form.instance.user = self.request.user
        street_1 = form.instance.address_line_1
        street_1_formatted = street_1.replace(' ', '%20')
        street_2 = form.instance.address_line_2
        start_date = form.instance.start_date
        end_date = form.instance.end_date
        city = form.instance.city
        state = form.instance.state
        request_string = f"https://us-street.api.smartystreets.com/street-address?auth-id={os.environ['SS_AUTH_ID']}&auth-token={os.environ['SS_AUTH_TOKEN']}&street={street_1_formatted}&street2=&city={city}&state={state}&zipcode=&address-type=us-street-components"
        unparsed_formatted_address = requests.get(request_string)
        parsed_formatted_address = json.loads(
            unparsed_formatted_address.content)
        if len(parsed_formatted_address) < 1:
            print('invalid address')
            return redirect('invalid_address')
        form.instance.address_line_1 = parsed_formatted_address[0]['delivery_line_1']
        form.instance.address_line_2 = street_2
        form.instance.city = parsed_formatted_address[0]['components']['city_name']
        form.instance.state = parsed_formatted_address[0]['components']['state_abbreviation']
        form.instance.zipcode = parsed_formatted_address[0]['components']['zipcode']
        form.instance.latitude = parsed_formatted_address[0]['metadata']['latitude']
        form.instance.longitude = parsed_formatted_address[0]['metadata']['longitude']
        form.instance.start_date = start_date
        form.instance.end_date = end_date
        form.instance.static_map_url = self.build_static_map_url(
            form.instance.latitude, form.instance.longitude, os.environ['STATIC_MAPS_KEY'])
        form.instance.static_streetview_url = self.build_static_streetview_url(
            form.instance.latitude, form.instance.longitude, os.environ['STREETVIEW_KEY'])
        if 'addnew' in form.data:
            self.success_url = '/select_entry_form/'
            return super().form_valid(form)
        elif 'detail' in form.data:
            return super().form_valid(form)


class WorkplaceUpdate(LoginRequiredMixin, UpdateView):
    model = Workplace
    fields = ['address_line_1', 'address_line_2', 'city', 'state', 'start_date', 'end_date',
              'company_name', 'employer_name', 'employer_number', 'employer_email', 'title']

    def build_static_map_url(self, lat, long, key):
        url = f'https://maps.googleapis.com/maps/api/staticmap?center={lat},{long}&zoom=13&size=600x300&maptype=roadmap&markers=color:purple%7Clabel:%7C{lat},{long}&key={key}'
        return url

    def build_static_streetview_url(self, lat, long, key):
        url = f'https://maps.googleapis.com/maps/api/streetview?size=600x300&location={lat},{long}&heading=&pitch=0&key={key}'
        return url

    def form_valid(self, form):
        form.instance.user = self.request.user
        street_1 = form.instance.address_line_1
        street_1_formatted = street_1.replace(' ', '%20')
        street_2 = form.instance.address_line_2
        start_date = form.instance.start_date
        end_date = form.instance.end_date
        city = form.instance.city
        state = form.instance.state
        request_string = f"https://us-street.api.smartystreets.com/street-address?auth-id={os.environ['SS_AUTH_ID']}&auth-token={os.environ['SS_AUTH_TOKEN']}&street={street_1_formatted}&street2=&city={city}&state={state}&zipcode=&address-type=us-street-components"
        unparsed_formatted_address = requests.get(request_string)
        parsed_formatted_address = json.loads(
            unparsed_formatted_address.content)
        if len(parsed_formatted_address) < 1:
            print('invalid address')
            return redirect('invalid_address')
        form.instance.address_line_1 = parsed_formatted_address[0]['delivery_line_1']
        form.instance.address_line_2 = street_2
        form.instance.city = parsed_formatted_address[0]['components']['city_name']
        form.instance.state = parsed_formatted_address[0]['components']['state_abbreviation']
        form.instance.zipcode = parsed_formatted_address[0]['components']['zipcode']
        form.instance.latitude = parsed_formatted_address[0]['metadata']['latitude']
        form.instance.longitude = parsed_formatted_address[0]['metadata']['longitude']
        form.instance.start_date = start_date
        form.instance.end_date = end_date
        form.instance.static_map_url = self.build_static_map_url(
            form.instance.latitude, form.instance.longitude, os.environ['STATIC_MAPS_KEY'])
        form.instance.static_streetview_url = self.build_static_streetview_url(
            form.instance.latitude, form.instance.longitude, os.environ['STREETVIEW_KEY'])
        return super().form_valid(form)


class WorkplaceDelete(LoginRequiredMixin, DeleteView):
    model = Workplace
    success_url = '/workplaces/'
# ---------------------- Auth Views -------------------------


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)
