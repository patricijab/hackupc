from django.shortcuts import render
from django.template import loader
from .models import Demand, Category, MenuItem

def index(request):
	#template = loader.get_template('index.html')
	category_list = Category.objects.all()
	menu = MenuItem.objects.all()
	demand = Demand.objects.all()
	context = {
		'categories': category_list,
		'menu': menu,
		'demand': demand
	}
	return render(request, 'index.html', context)