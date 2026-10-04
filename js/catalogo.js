const botones = document.querySelectorAll(".lista-catalogo button");
const nombre = document.querySelector("#nombre_animal");
const listaFiltros = document.querySelector("#lista_filtros");

let lista = [];

function recorrer_botones(boton) {
    boton.addEventListener("click", function () {
        if (boton.id == "buscar-nombre") {
            buscarNombre();
        }
        else {
            var encontrado = false;
            for (var i = 0; i < lista.length; i++) {
                if (lista[i] == boton) {
                    encontrado = true;
                    lista.splice(i, 1);
                    boton.classList.remove("borde");
                }
            }
            if (!encontrado) {
                lista.push(boton);
                boton.classList.add("borde");
            }
            mostrarFiltros();
        }
    });
}


function mostrarFiltros() {
    // chau html
    listaFiltros.innerHTML = "";
    // ponemos filtros a la lista
    lista.forEach(function agregar_botones(boton) {
        const li = document.createElement("li");
        li.classList.add("filtro-lista");
        if (boton.id == "buscar-nombre") {
            li.textContent = "Nombre: " + nombre.value;
        }
        else {
            li.textContent = boton.textContent;
        }
        // toco filtro borro filtro
        li.addEventListener("click", function borrar_boton() {
            var encontrado = false;
            for (var i = 0; i < lista.length; i++) {
                if (lista[i] == boton) {
                    encontrado = true;
                    lista.splice(i, 1);
                    boton.classList.remove("borde");
                }
            }
            if (encontrado) {
                mostrarFiltros();
            }
        });
        listaFiltros.appendChild(li);
    });
}

function buscarNombre() {
    var encontrado = false;
    for (var i = 0; i < lista.length; i++) {
        if (lista[i].id == "buscar-nombre") {
            encontrado = true;
        }
    }
    if (nombre.value != "") {
        if (encontrado == false) {
            lista.push(document.querySelector("#buscar-nombre"));
        }
        mostrarFiltros();
    }
}

function iniciarValidacion() {
    botones.forEach(recorrer_botones);
}

iniciarValidacion();
