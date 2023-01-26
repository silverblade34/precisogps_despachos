
const abrirModal = (message, status) =>{
    if (status == "true"){
        swal ( " ¡Buen trabajo! " , message, "success")   ;
    }else{
        swal ( " ¡Ocurrio un error! " , message, "error")   ;
    }      
}

const btns4 = document.querySelectorAll(".btn-preciso-4");
const hiddenLoa4 = document.getElementById("hidden-loader-4");

btns4.forEach(btn4 => {
	btn4.addEventListener("click", function(){
		// Mostrando el div
		hiddenLoa4.style.display = "flex";
	});

})


// const btns5 = document.querySelectorAll(".btn-preciso-5");
// const hiddenLoa5 = document.getElementById("hidden-loader-5");

// btns5.forEach(btn5 => {
// 	btn5.addEventListener("click", function(){
// 		// Mostrando el div
// 		hiddenLoa5.style.display = "flex";
// 	});

// })
