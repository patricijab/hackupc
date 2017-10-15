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