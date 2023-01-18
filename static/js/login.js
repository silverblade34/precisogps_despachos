const sign_in_btn = document.querySelector('#sign-in-btn');
const sign_up_btn = document.querySelector('#sign-up-btn');
const container = document.querySelector('.container');

sign_up_btn.addEventListener('click', () => {
  container.classList.add('sign-up-mode');
});

sign_in_btn.addEventListener('click', () => {
  container.classList.remove('sign-up-mode');
});


const btn = document.getElementById("btn-ingresar-preciso");
const hiddenLoa = document.getElementById("hidden-loader");

btn.addEventListener("click", function(){
    // Mostrando el div
    hiddenLoa.style.display = "flex";
});
