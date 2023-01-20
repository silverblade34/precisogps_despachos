const allSideMenu = document.querySelectorAll('#sidebar .side-menu.top li a');

allSideMenu.forEach(item=> {
	const li = item.parentElement;

	item.addEventListener('click', function () {
		allSideMenu.forEach(i=> {
			i.parentElement.classList.remove('active');
		})
		li.classList.add('active');
	})
});




// TOGGLE SIDEBAR
const menuBar = document.querySelector('#content nav .bx.bx-menu');
const sidebar = document.getElementById('sidebar');

menuBar.addEventListener('click', function () {
	sidebar.classList.toggle('hide');
})







const searchButton = document.querySelector('#content nav form .form-input button');
const searchButtonIcon = document.querySelector('#content nav form .form-input button .bx');
const searchForm = document.querySelector('#content nav form');

searchButton.addEventListener('click', function (e) {
	if(window.innerWidth < 576) {
		e.preventDefault();
		searchForm.classList.toggle('show');
		if(searchForm.classList.contains('show')) {
			searchButtonIcon.classList.replace('bx-search', 'bx-x');
		} else {
			searchButtonIcon.classList.replace('bx-x', 'bx-search');
		}
	}
})





if(window.innerWidth < 768) {
	sidebar.classList.add('hide');
} else if(window.innerWidth > 576) {
	searchButtonIcon.classList.replace('bx-x', 'bx-search');
	searchForm.classList.remove('show');
}


window.addEventListener('resize', function () {
	if(this.innerWidth > 576) {
		searchButtonIcon.classList.replace('bx-x', 'bx-search');
		searchForm.classList.remove('show');
	}
})



const switchMode = document.getElementById('switch-mode');

switchMode.addEventListener('change', function () {
	if(this.checked) {
		document.body.classList.add('dark');
	} else {
		document.body.classList.remove('dark');
	}
})

// Ventana de loader

const btns = document.querySelectorAll(".btn-ingresar-preciso");
const hiddenLoa = document.getElementById("hidden-loader");

btns.forEach(btn => {
	btn.addEventListener("click", function(){
		// Mostrando el div
		hiddenLoa.style.display = "flex";
	});

})
// Ventana de loader

// Ventana de progress bar

const btnprogress = document.querySelectorAll(".btn-progress-bar");
const ventanaprogress = document.getElementById("progress-bar");

btnprogress.forEach(btnpr => {
	btnpr.addEventListener("click", function(){
		// Mostrando el div
		ventanaprogress.style.display = "block";
	});
})

// Ventana de loader

// Message alert de mostrar placas en despachos
var btnplacas = document.getElementById("btn-message-placas");
  var alertplacas = document.getElementById("alert-message-placas");

  btnplacas.addEventListener("click", function() {
    alertplacas.style.display = "none";
  });

// Message alert de mostrar placas en despachos

