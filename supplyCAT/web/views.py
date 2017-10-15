from django.shortcuts import render
from django.template import loader
from .models import Demand, Category, MenuItem
import csv
import json
from sklearn import linear_model, cross_validation
import numpy as np
import matplotlib.pyplot as plt
import datetime


#foo_instance = Category.objects.create(category='test')
def prepare_data(r):
    row = []
    # ure
    for i in range(8, 22):
        if (int(r[0]) == i):
            row.append(1)
        else:
            row.append(0)
    # dan v tednu
    for i in range(7):
        if (int(r[1]) == i):
            row.append(1)
        else:
            row.append(0)
    # vikend
    if (int(r[1]) > 4):
        row.append(1)
    else:
        row.append(0)
    # mesec
    """
    for i in range(12):
        if (r[2] == i):
            row.append(1)
        else:
            row.append(0)
    """
    # item
    for i in range(10):
        if (int(r[4]) == i):
            row.append(1)
        else:
            row.append(0)
    return row
data = []
y = []
with open('web/static/data_02.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for r in reader:
        row = prepare_data(r)
        data.append(row)
        y.append(int(r[5]))
lm = linear_model.LinearRegression()
model = lm.fit(data,y)

def read_c(filename):
	result = []
	with open(filename, newline='') as csvfile:
		spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
		for row in spamreader:
			result.append(row[0].split(','))
	return result
data = read_c('web/static/data_02.csv')
"""for d in range(len(data)):
	haha = int(data[d][4]) + 1
	print(haha)
	item1 = MenuItem.objects.get(pk=haha)
	instance = Demand.objects.create(itemId = item1, month = int(data[d][2]), hour = int(data[d][0]), dayType = int(data[d][1]), supply= int(data[d][5]))
"""
def avgMonth(item):
	suma = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	q = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	for i in range(len(data)):
		if (data[i][4] == item):
			suma[int(data[i][2])-1] += int(data[i][5])
			q[int(data[i][2])-1] += 1
	for l in range(len(suma)):
		if (q[l] != 0):
			suma[l] = int(suma[l]/q[l])
	return suma

def avgDay(item):
	suma = [0, 0, 0, 0, 0, 0, 0]
	q = [0, 0, 0, 0, 0, 0, 0]
	for i in range(len(data)):
		if (data[i][4] == item):
			suma[int(data[i][1])] += int(data[i][5])
			q[int(data[i][1])] += 1
	for l in range(len(suma)):
		if (q[l] != 0):
			suma[l] = int(suma[l]/q[l])
	return suma

def avgHour(item):
	suma = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	q = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	for i in range(len(data)):
		if (data[i][4] == item):
			suma[int(data[i][0])-7] += int(data[i][5])
			q[int(data[i][0])-7] += 1
	for l in range(len(suma)):
		if (q[l] != 0):
			suma[l] = int(suma[l]/q[l])
	return suma

def prediction():
	result = []
	now = datetime.datetime.now()
	print(now)
	hour = now.hour
	print(hour)
	dayWeek = now.weekday()
	print(dayWeek)
	month = now.month
	year = now.year
	for i in range(10):
		ss = [0, 0, 0]
		suma1 = 0
		for k in range(7, 23):
			suma1 += lm.predict(prepare_data([k, dayWeek, month, year, i]))
		ss[0] = int(suma1/16)
		#result[0].append(lm.predict(prepare_data([hour, dayWeek, month, year, i])))
		suma = 0
		for j in range(7):
			for k in range(7, 23):
				suma += int(lm.predict(prepare_data([k, j, month, year, i])))
		ss[1] = int(suma/(16))
		ss[2] = int((suma/16)*(30/7))
		result.append(ss)
	return result

def index(request):
	category_list = Category.objects.all()
	menu = MenuItem.objects.all()
	demand = list(Demand.objects.all())
	print(demand)
	data2 = {
		"Croissant": [avgMonth('0'), avgDay('0'), avgHour('0')], 
		"Muffin": [avgMonth('1'), avgDay('1'), avgHour('1')], 
		"Capuccino": [avgMonth('2'), avgDay('2'), avgHour('2')], 
		"Sandwich": [avgMonth('3'), avgDay('3'), avgHour('3')], 
		"Tea": [avgMonth('4'), avgDay('4'), avgHour('4')], 
		"Juice": [avgMonth('5'), avgDay('5'), avgHour('5')], 
		"Toast": [avgMonth('6'), avgDay('6'), avgHour('6')], 
		"Water": [avgMonth('7'), avgDay('7'), avgHour('7')], 
		"Cafe Latte": [avgMonth('8'), avgDay('8'), avgHour('8')], 
		"Espresso": [avgMonth('9'), avgDay('9'), avgHour('9')]
	}
	data = json.dumps(data2)
	lala = prediction()
	lala2 = {
		"Croissant": lala[0], 
		"Muffin": lala[1], 
		"Capuccino": lala[2], 
		"Sandwich": lala[3], 
		"Tea": lala[4], 
		"Juice": lala[5], 
		"Toast": lala[6], 
		"Water": lala[7], 
		"Cafe Latte": lala[8], 
		"Espresso": lala[9]
	}
	lala = json.dumps(lala2)
	return render(request, 'index.html', {"data2": data, "categories": category_list, "menu": menu, "prediction": lala})