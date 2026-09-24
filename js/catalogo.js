const botones = document.querySelectorAll(".lista-catalogo button");
const buscar = document.querySelector("#buscar-nombre");
const nombre = document.querySelector("#nombre_animal");

function recorrer_botones(boton) {
    boton.addEventListener("click", function () {

        botones.forEach(function (boton) {
            boton.classList.remove("borde");
        });

        boton.classList.add("borde");

        if (boton.id == "buscar-nombre") {
            ver_input();
        }
        else {
            alert("Elegiste: " + boton.textContent);
        }
    });
}

function ver_input() {
    alert("Buscaste: " + nombre.value);
}

function iniciarValidacion() {
    botones.forEach(recorrer_botones);
}

iniciarValidacion()
