const botones = document.querySelectorAll(".lista-catalogo button");
const nombre = document.querySelector("#nombre_animal");
const boton_nombre = document.querySelector("#buscar-nombre")
const borrar_mascota = document.querySelectorAll(".borrar")
const panelFiltros = document.getElementById("panel_filtros");
const abrir_filtro = document.getElementById("abrir-filtros")
const cerrar_filtro = document.getElementById("cerrar-filtros")
const fondo_filtro = document.getElementById("fondo-filtros")

function boton_seleccionado() {
    this.classList.toggle("catalogo-boton-activo")
}

function boton_borrar() {
    alert(nombre.value)
    this.classList.toggle("catalogo-boton-activo")
}

function boton_borrar_mascota() {
    let valor = confirm("¿Estás seguro de que quieres borrar esta mascota?")
    if (valor) {
        alert("Mascota borrada")
    }
}

function cambiar_filtro() {
    panelFiltros.classList.toggle("abierto");
}

function iniciarValidacion() {
    for (i = 0; i < botones.length; i++) {
        botones[i].addEventListener("click", boton_seleccionado)
    }
    boton_nombre.addEventListener("click", boton_borrar)
    for (i = 0; i < borrar_mascota.length; i++) {
        borrar_mascota[i].addEventListener("click", boton_borrar_mascota)
    }
    abrir_filtro.addEventListener("click", cambiar_filtro);
    cerrar_filtro.addEventListener("click", cambiar_filtro);
    fondo_filtro.addEventListener("click", cambiar_filtro);

}
iniciarValidacion()