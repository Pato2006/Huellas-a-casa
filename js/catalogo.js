const botones = document.querySelectorAll(".lista-catalogo button");
const nombre = document.querySelector("#nombre_animal");
const boton_nombre = document.querySelector("#buscar-nombre")

function boton_seleccionado() {
    this.classList.toggle("catalogo-boton-activo")
}

function boton_borrar(){
    alert(nombre.textContent)
    this.classList.toggle("catalogo-boton-activo")
}

function iniciarValidacion() {
    for (i = 0; i < botones.length; i++) {
        botones[i].addEventListener("click", boton_seleccionado)
    }
    boton_nombre.addEventListener("click",boton_borrar)
}
iniciarValidacion()