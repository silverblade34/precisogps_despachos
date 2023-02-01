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



// Ventana de loader

const btns = document.querySelectorAll(".btn-ingresar-preciso");
const hiddenLoa = document.getElementById("hidden-loader");

btns.forEach(btn => {
	btn.addEventListener("click", function(){
		console.log("----------------------------1")
		// Mostrando el div
		hiddenLoa.style.display = "flex";
	});

})
// Ventana de loader

// Ventana de progress bar

// const btnprogress2 = document.getElementById("btn-progress-bar-2");
// const ventanaprogress2 = document.getElementById("progress-bar-2");

// btnprogress2.addEventListener("click", function(){
//     // Mostrando el div
//     ventanaprogress2.style.display = "block";
// });

const btnprogress2  = document.querySelectorAll(".btn-progress-bar-2");
const ventanaprogress2 = document.getElementById("progressbar2");

btnprogress2.forEach(btnp => {
	btnp.addEventListener("click", function(){
		console.log("----------------------------1")
		// Mostrando el div
		ventanaprogress2.style.display = "block";
	});

})




