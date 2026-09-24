const botones = document.querySelectorAll(".lista-catalogo button");
const nombre = document.querySelector("#nombre_animal");
const listaFiltros = document.querySelector("#lista_filtros");

let lista = [];

function recorrer_botones(boton) {
    boton.addEventListener("click", function () {

        if (lista.includes(boton)) {
            // Ya estaba seleccionado → eliminar
            lista = lista.filter(item => item !== boton);
            boton.classList.remove("borde");
        } else {
            // No estaba seleccionado → agregar
            lista.push(boton);
            boton.classList.add("borde");
        }

        mostrarFiltros();

        if (boton.id == "buscar-nombre") {
            ver_input();
        }
    });
}

function mostrarFiltros() {
    // Limpiamos la lista HTML
    listaFiltros.innerHTML = "";

    // Agregamos cada filtro seleccionado
    lista.forEach(function (boton) {
        const li = document.createElement("li");

        li.textContent = boton.textContent;

        // Al tocar el filtro, también se elimina
        li.addEventListener("click", function () {
            lista = lista.filter(item => item !== boton);
            boton.classList.remove("borde");

            mostrarFiltros();
        });

        listaFiltros.appendChild(li);
    });
}

function ver_input() {
    alert("Buscaste: " + nombre.value);
}

function iniciarValidacion() {
    botones.forEach(recorrer_botones);
}

iniciarValidacion();

