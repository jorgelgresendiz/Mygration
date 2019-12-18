from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
import os
import requests
import json
from .models import Residence, Workplace


def home(request):
    return render(request, 'index.html')

# ---------------------- Residence Views -------------------------


class ResidenceList(ListView):
    model = Residence


class ResidenceDetail(DetailView):
    model = Residence


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
	new_residence.save()
	return redirect('residences/')
    
    
# ---------------------- Workplace Views -------------------------


class WorkplaceList(ListView):
    model = Workplace


class WorkplaceDetail(DetailView):
    model = Workplace


def create_workplace(request):
    pass
