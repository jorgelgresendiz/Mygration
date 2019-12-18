from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
import os
import requests
import json
from .models import Residence, Workplace


# ---------------------- Generic Views ---------------------------

def home(request):
    return render(request, 'index.html')

# ---------------------- Residence Views -------------------------

@login_required
def residences_index(request):
    residence = Residence.objects.filter(user=request.user)
    return render(request, 'residences/residences_index.html', {'residence': residence})


@login_required
def residence_detail(request, residence_id):
    residence = Residence.objects.get(id=residence_id)
    return render(request, 'residences/residence_detail.html', {
        'residence': residence})
    
@login_required
def create_residence(request):
	new_residence = Residence.create()
	input_address = request.POST
	street_1 = input_address.street1
	street_1_formatted = street_1.replace(' ', '%20')
	street_2 = input_address.street2
	start_date = input_address.start_date
	end_date = input_address.end_date
	city = input_address.city
	state = input_address.state
	request_string = f'https://us-street.api.smartystreets.com/street-address?auth-id={os.environ['SS_AUTH_ID']}&auth-token={os.environ['SS_AUTH_TOKEN']}&street={street_1_formatted}&street2=&city={city}&state={state}&zipcode=&address-type=us-street-components'
	unparsed_formatted_address = requests.get(request_string)
	parsed_formatted_address = json.loads(
        unparsed_formatted_address.content)
	new_residence.address_line_1 = parsed_formatted_address[0]['delivery_line_1']
	new_residence.address_line_2 = street_2
	new_residence.city = parsed_formatted_address[0]['components']['city_name']
	new_residence.state = parsed_formatted_address[0]['components']['state_abbreviation']
	new_residence.latitude = parsed_formatted_address[0]['metadata']['latitude']
	new_residence.longitude = parsed_formatted_address[0]['metadata']['longitude']
	new_residence.start_date = start_date
	new_residence.end_date = end_date
	new_residence.user = request.user
	new_residence.save()
	print(f'Saving new residence: {new_residence}')
	return redirect('residences/')
    
    
# ---------------------- Workplace Views -------------------------

@login_required
def workplaces_index(request):
    workplace = Workplace.objects.filter(user=request.user)
    return render(request, 'workplaces/workplaces_index.html', {'workplace': workplace})


@login_required
def workplace_detail(request, workplace_id):
    workplace = Workplace.objects.get(id=workplace_id)
    return render(request, 'workplaces/workplace_detail.html', {
        'workplace': workplace})


@login_required
def create_workplace(request):
    pass


# ---------------------- Auth Views -------------------------

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)