google.charts.load('current', {'packages':['corechart']});
google.charts.setOnLoadCallback(drawMonths);
google.charts.setOnLoadCallback(drawDays);
google.charts.setOnLoadCallback(drawHours);

function drawMonths() {
	var data = google.visualization.arrayToDataTable([
	  ['Month',  'Croissant', 'Muffin', 'Capuccino', 'Sandwich', 'Tea', 'Juice', 'Toast', 'Water', 'Cafe Latte', 'Espresso'],
	  ['Jan', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
	  ['Feb', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
	  ['Mar', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
	  ['Apr', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
	  ['Junr', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
	  ['Jul', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
	  ['Aug', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
	  ['Sep', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
	  ['Oct', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
	  ['Nov', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
	  ['Dec', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	]);

	var options = {
	  title: 'Demand by months',
	  height: 370,
	  isStacked: true,
	  vAxis: {minValue: 0},
	  connectSteps: false,
      colors: ['#4374E0', '#53A8FB', '#F1CA3A', '#E49307'],
      legend: { position: 'bottom', maxLines: 2}
	};

	var chart = new google.visualization.SteppedAreaChart(document.getElementById('chart_div'));

	chart.draw(data, options);
}

function drawDays() {
	var data = google.visualization.arrayToDataTable([
	  ['Day',  'Croissant', 'Muffin', 'Capuccino', 'Sandwich', 'Tea', 'Juice', 'Toast', 'Water', 'Cafe Latte', 'Espresso'],
	  ['Mon', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
	  ['Tue', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
	  ['Wed', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
	  ['Thu', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
	  ['Fri', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
	  ['Sat', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
	  ['Sun/Holiday', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	]);

	var options = {
	  title: 'Demand by week days & holidays',
	  isStacked: true,
	  height: 370,
	  vAxis: {minValue: 0},
	  connectSteps: false,
      colors: ['#4374E0', '#53A8FB', '#F1CA3A', '#E49307'],
      legend: { position: 'bottom', maxLines: 2}
	};

	var chart = new google.visualization.SteppedAreaChart(document.getElementById('chart_div2'));

	chart.draw(data, options);
}

function drawHours() {
	var data = google.visualization.arrayToDataTable([
	  ['Hour', 'Croissant', 'Muffin', 'Capuccino', 'Sandwich', 'Tea', 'Juice', 'Toast', 'Water', 'Cafe Latte', 'Espresso'],
	  ['00', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
	  ['01', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
	  ['02', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
	  ['03', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
	  ['04', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
	  ['05', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
	  ['06', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
	  ['07', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
	  ['08', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
	  ['09', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
	  ['10', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
	  ['11', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
	  ['12', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
	  ['13', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
	  ['14', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
	  ['15', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
	  ['16', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
	  ['17', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
	  ['18', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
	  ['19', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
	  ['20', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
	  ['21', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
	  ['22', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
	  ['23', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	]);

	var options = {
	  title: 'Demand by hour of day',
	  curveType: 'function',
	  height: 370,
	  vAxis: {minValue: 0},
	  connectSteps: false,
      colors: ['#4374E0', '#53A8FB', '#F1CA3A', '#E49307'],
      legend: { position: 'bottom', maxLines: 2},
      explorer: { keepInBounds: true },
      hAxis: { viewWindow: {max: 22, min: 8} }
	};

	var chart = new google.visualization.LineChart(document.getElementById('chart_div3'));

	chart.draw(data, options);
}

function on_stat() {
	document.getElementById("Plan").style.display = "none";
	document.getElementById("Report").style.display = "none";
    document.getElementById("Statistics").style.display = "block";
    addClass("st", "dark");
    removeClass("pl", "dark");
    removeClass("re", "dark");
    addClass("re", "color");
    removeClass("st", "color");
    addClass("pl", "color");
}

function on_plan() {
	document.getElementById("Report").style.display = "none";
	document.getElementById("Statistics").style.display = "none";
    document.getElementById("Plan").style.display = "block";
    addClass("pl", "dark");
    removeClass("st", "dark");
    removeClass("re", "dark");
    addClass("st", "color");
    removeClass("pl", "color");
    addClass("re", "color");
}

function on_report() {
	document.getElementById("Plan").style.display = "none";
	document.getElementById("Statistics").style.display = "none";
    document.getElementById("Report").style.display = "block";
    addClass("re", "dark");
    removeClass("st", "dark");
    removeClass("pl", "dark");
    addClass("st", "color");
    removeClass("re", "color");
    addClass("pl", "color");
}

function off() {
    document.getElementById("Statistics").style.display = "none";
    document.getElementById("Plan").style.display = "none";
	document.getElementById("Report").style.display = "none";
	removeClass("pl", "dark");
    removeClass("st", "dark");
    removeClass("re", "dark");
    addClass("st", "color");
    addClass("re", "color");
    addClass("pl", "color");
}

function div_hide(id){
    document.getElementById(id).style.display = "none";
}

function div_show(id) {
    document.getElementById(id).style.display = "block";
}

function addClass(id, clas) {
	if ( !document.getElementById(id).classList.contains(clas) ) {
		document.getElementById(id).classList.add(clas);
	}
}
function removeClass(id, clas) {
	if ( document.getElementById(id).classList.contains(clas) ) {
		document.getElementById(id).classList.remove(clas);
	}
}