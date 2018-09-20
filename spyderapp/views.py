from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from .models import Patron, Associates

from django.http import HttpResponse
from django.views.generic import View

from .utils import render_to_pdf #created in step 4


class GeneratePdf(View):
	def get(self, request, *args, **kwargs):
		data = {
			'amount': 39.99,
			'customer_name': 'Cooper Mann',
			'order_id': 1233434,
		}
		pdf = render_to_pdf('report_view.html', data)
		return HttpResponse(pdf, content_type='application/pdf')


class RegisterPatron(CreateView):
    model = Patron
    fields = [
    	'patron_id',
    	'first_name',
    	'last_name',
    	'date_of_birth',
    	'age',
    	'contact_number',
    	'current_address',
    	'email_id',
    	'associated_names',
    	'previous_addresses',
    	'possible_relatives',
    	'possible_associates',
    	'possible_businesses',
    	'cases',
    	'links',
    ]
    success_url = '/reg_success/'

