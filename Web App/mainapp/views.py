from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
#from similarity_check.py import similarity_check
from .similarity_check import *
import json

def index(request):
	return render(request, 'index.html')

def service(request):
	return render(request, 'service.html')

def about(request):
	return render(request, 'about.html')

def contact(request):
	return render(request, 'contact.html')

def registered_categories(request):

	data = Category.objects.all()

	category_data = []
	for dict in data:
		val1 = dict.category_name
		category_data.append({'category_name': val1})

	print(category_data)

	return render(request, 'registered_categories.html', {'category_data': category_data})

def new_category(request):
	if request.method == "POST":
		form = CategoryForm(request.POST)

		if form.is_valid():
			form.save()
			return redirect('service')

	else:
		form = CategoryForm()
		return render(request, 'new_category.html', {'form' : form})

def items(request, value):

	data = Item.objects.all()

	items_data = []
	for dict in data:
		val1 = dict.category_name
		val2 = dict.item_name
		val3 = dict.item_description
		val4 = dict.founder_name
		val5 = dict.founder_number
		if val1 == value:
			items_data.append({'category_name': val1,
							   'item_name': val2, 'item_description': val3,
							   'founder_name': val4, 'founder_number': val5})

	print(items_data)

	return render(request, 'items.html', {'items_data': items_data})

def add_item(request):
	if request.method == "POST":
		form = ItemForm(request.POST)

		if form.is_valid():
			form.save()
			return redirect('service')

	else:
		form = ItemForm()
		return render(request, 'add_item.html', {'form' : form})

def filtered_items(request, value):

	if request.method == 'POST':
		#Lost Item description data
		description = request.POST.get('description', None)

		# All the data
		data = Item.objects.all()

		print('Data: ', data)

		items_data = []
		for dict in data:
			val1 = dict.category_name
			val2 = dict.item_name
			val3 = dict.item_description
			val4 = dict.founder_name
			val5 = dict.founder_number
			if val1 == value:
				items_data.append({'category_name': val1,
								   'item_name': val2, 'item_description': val3,
								   'founder_name': val4, 'founder_number': val5})

		print('Items Data: ', items_data)

		answers = similarity_check(description, items_data)

		print(answers)

		# response = [
		# {
		# 	'msg': 'Message from Point 1: Form has been successfully submitted',
		# 	'description': description
		# },
		# {
		# 	'msg': 'Message from Point 2: Form has been successfully submitted',
		# 	'description': description
		# },
		# ]
		return JsonResponse(answers, safe=False)

	return render(request, 'filtered_items.html')

