

const btns2 = document.querySelectorAll(".btn-preciso-2");
const hiddenLoa2 = document.getElementById("hidden-loader");

btns2.forEach(btn2 => {
  btn2.addEventListener("click", function () {
    // Mostrando el div
    hiddenLoa2.style.display = "flex";
  });

})


// // Ventana de progress bar

// const btnprogress = document.getElementById("btn-progress-bar");
// const ventanaprogress = document.getElementById("progress-bar");

// btnprogress.addEventListener("click", function(){
// 		// Mostrando el div
// 		ventanaprogress.style.display = "block";
// });



// Message alert de mostrar placas en despachos
var btnplacas = document.getElementById("btn-message-placas");
var alertplacas = document.getElementById("alert-message-placas");

btnplacas.addEventListener("click", function () {
  alertplacas.style.display = "none";
});

// Message alert de mostrar placas en despachos
