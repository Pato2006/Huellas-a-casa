const botones = document.querySelectorAll(".lista-catalogo button");
const nombre = document.querySelector("#nombre_animal");
const boton_nombre = document.querySelector("#buscar-nombre")

const panelFiltros = document.getElementById("panel_filtros");
const abrir_filtro = document.getElementById("abrir-filtros")
const cerrar_filtro = document.getElementById("cerrar-filtros")

function boton_seleccionado() {
    this.classList.toggle("catalogo-boton-activo")
}

function boton_busqueda() {
    alert(nombre.value)
    this.classList.toggle("catalogo-boton-activo")
}

function cambiar_filtro() {
    panelFiltros.classList.toggle("abierto");
}

function iniciarValidacion() {
    for (i = 0; i < botones.length; i++) {
        botones[i].addEventListener("click", boton_seleccionado)
    }
    boton_nombre.addEventListener("click", boton_busqueda)
    abrir_filtro.addEventListener("click", cambiar_filtro);
    cerrar_filtro.addEventListener("click", cambiar_filtro);
}
iniciarValidacion()