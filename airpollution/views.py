from django.shortcuts import render
from django import forms
import openpyxl

from airpollution.models import Pollutant, Country
from airpollution.helpers import get_headers_and_units


# Create your views here.

# take the form from the HTML form
class ExcelUploadForm(forms.Form):
    year = forms.CharField(max_length=4)
    file = forms.FileField()


def welcome(request):
    context = {
        'app_name': request.resolver_match.app_name
    }

    return render(request, 'airpollution/welcome.html', context)


""" we pass context -> if the page request.path is /airpollution, do this in navbar, or
 do something else in navbar"""


def upload_file(request):
    # accept only method POST
    if request.method == 'POST':
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            wb = openpyxl.load_workbook(filename=file, read_only=False)
            tab_names = wb.get_sheet_names()
            """get tab names from Excel file"""
            for tab_name in tab_names:
                ws = wb[tab_name]
                """ take each worksheet and analyze them"""
                pollutant_name = tab_name.split('_')[0]
                """extract info from that worksheet
                tab_name.sp^lit('_') -> remove _ from the name.
                [0] -> get the first item only from the name
                ex: PM10_station_statistics -> it splits in 3 words -> 
                PM10 , station, statistics. We keep only PM10 which is first
                item [0]"""

                # Create a pollutant that is stored in our database
                pollutant = Pollutant.objects.get_or_create(name=pollutant_name)
                """ If pollutant name is in Excel file, get it. If it's not
                create it."""
                headers_row, headers, units = get_headers_and_units(ws)
                print('test')
    else:
        pass
    """get file out of this form. It's an object
    ['file'] name is same name we put in name="file" in welcome.html
    <input class="form-control" id="file" name="file" type="file"""
    context = {
        'message_success': 'file uploaded successfully',
        'app_name': request.resolver_match.app_name
    }
    return render(request, 'airpollution/welcome.html', context)


""" pass -> if error, it will not give an error, but does nothing"""


def temp_country_creator(request):
    countries = {
        'Albania': 'AL',
        'Andorra': 'AD',
        'Austria': 'AT',
        'Belgium': 'BE',
        'Bosnia and Herzegovina': 'BA',
        'Bulgaria': 'BG',
        'Croatia': 'HR',
        'Cyprus': 'CY',
        'Czech Republic': 'CZ',
        'Denmark': 'DK',
        'Estonia': 'EE',
        'Finland': 'FI',
        'France': 'FR',
        'Germany': 'DE',
        'Greece': 'GR',
        'Hungary': 'HU',
        'Iceland': 'IS',
        'Ireland': 'IE',
        'Italy': 'IT',
        'Kosovo under UNSCR 1244/99': 'XK',
        'Latvia': 'LV',
        'Lithuania': 'LT',
        'Luxembourg': 'LU',
        'Malta': 'MT',
        'Montenegro': 'ME',
        'Netherlands': 'NL',
        'Norway': 'NO',
        'Poland': 'PL',
        'Portugal': 'PT',
        'Romania': 'RO',
        'Serbia': 'RS',
        'Slovakia': 'SK',
        'Slovenia': 'SI',
        'Spain': 'ES',
        'Sweden': 'SE',
        'Switzerland': 'CH',
        'The former Yugoslav Republic of Macedonia': 'MK',
        'Turkey': 'TR',
        'United Kingdom': 'GB',
    }

    # insert all entries in list
    to_insert = []
    # iterate through countries dictionary
    for country_name, iso_code in countries.items():
        to_insert.append(Country(iso_code=iso_code, name=country_name))
    Country.objects.bulk_create(to_insert)
    """ quick way to sending lots of entries
     We put all the countries in the to_insert list []. Nothing is saved yet. Then we create
     all of them with bulk_create to save once. Instead of saving each country entry one by 
     one. """

    context = {
        'message_success': 'Countries created successfully',
        'app_name': request.resolver_match.app_name
    }
    return render(request, 'airpollution/welcome.html', context)


