const PATRON_EDAD = /^\d{1,2}$/;           // 0 a 99, solo dígitos
const PATRON_PESO = /^\d+(\.\d+)?$/;       // Ej: 8 o 8.5

const formulario = document.querySelector(".formulario");

const nombre = document.querySelector("#nombre");
const edad = document.querySelector("#edad");
const peso = document.querySelector("#peso");
const personalidad = document.querySelector("#personalidad");
const descripcion = document.querySelector("#descripcion");
const foto = document.querySelector("#foto");

const errorNombre = document.querySelector("#error-nombre");
const errorEdad = document.querySelector("#error-edad");
const errorPeso = document.querySelector("#error-peso");
const errorPersonalidad = document.querySelector("#error-personalidad");
const errorDescripcion = document.querySelector("#error-descripcion");
const errorTipo = document.querySelector("#error-tipo");
const errorEstado = document.querySelector("#error-estado");


// =========================
// VALIDAR NOMBRE
// =========================

function validarNombre() {
    const nombreLimpio = nombre.value.trim();
    let esValido = false;

    if (nombreLimpio.length >= 3) {
        nombre.classList.remove("invalido");
        errorNombre.textContent = "";
        esValido = true;
    } else {
        nombre.classList.add("invalido");
        errorNombre.textContent = "Ingresá al menos 3 caracteres.";
    }

    return esValido;
}


// =========================
// VALIDAR EDAD
// =========================

function validarEdad() {
    const edadLimpia = edad.value.trim();
    let esValido = false;

    if (PATRON_EDAD.test(edadLimpia)) {
        edad.classList.remove("invalido");
        errorEdad.textContent = "";
        esValido = true;
    } else {
        edad.classList.add("invalido");
        errorEdad.textContent = "Ingresá una edad válida entre 0 y 99.";
    }

    return esValido;
}


// =========================
// VALIDAR PESO
// =========================

function validarPeso() {
    const pesoLimpio = peso.value.trim();
    let esValido = false;

    if (PATRON_PESO.test(pesoLimpio)) {
        peso.classList.remove("invalido");
        errorPeso.textContent = "";
        esValido = true;
    } else {
        peso.classList.add("invalido");
        errorPeso.textContent = "Ingresá un peso válido. Ejemplo: 8 o 8.5.";
    }

    return esValido;
}


// =========================
// VALIDAR PERSONALIDAD
// =========================

function validarPersonalidad() {
    const personalidadLimpio = personalidad.value.trim();
    let esValido = false;

    if (personalidadLimpio.length >= 12) {
        personalidad.classList.remove("invalido");
        errorPersonalidad.textContent = "";
        esValido = true;
    } else {
        personalidad.classList.add("invalido");
        errorPersonalidad.textContent = "Ingresá al menos 12 caracteres.";
    }

    return esValido;
}


// =========================
// VALIDAR DESCRIPCIÓN
// =========================

function validarDescripcion() {
    const descripcionLimpio = descripcion.value.trim();
    let esValido = false;

    if (descripcionLimpio.length >= 12) {
        descripcion.classList.remove("invalido");
        errorDescripcion.textContent = "";
        esValido = true;
    } else {
        descripcion.classList.add("invalido");
        errorDescripcion.textContent = "Ingresá al menos 12 caracteres.";
    }

    return esValido;
}


// =========================
// VALIDAR TIPO
// =========================

function validarTipo() {
    const tipoSeleccionado = document.querySelector(
        'input[name="tipo"]:checked'
    );

    let esValido = false;

    if (tipoSeleccionado !== null) {
        errorTipo.textContent = "";
        esValido = true;
    } else {
        errorTipo.textContent = "Seleccioná un tipo.";
    }

    return esValido;
}


// =========================
// VALIDAR ESTADO
// =========================

function validarEstado() {
    const estadoSeleccionado = document.querySelector(
        'input[name="estado"]:checked'
    );

    let esValido = false;

    if (estadoSeleccionado !== null) {
        errorEstado.textContent = "";
        esValido = true;
    } else {
        errorEstado.textContent = "Seleccioná un estado.";
    }

    return esValido;
}

function validarFoto() {
    esValido = false
    if (foto.files.length > 0) {
        alert("Foto valida.");
        esValido = true;
    }
    else {
        alert("Foto invalida")
    }

    return esValido;
}

// =========================
// VALIDAR FORMULARIO
// =========================

function validarFormulario(evento) {

    const nombreValido = validarNombre();
    const edadValida = validarEdad();
    const pesoValido = validarPeso();
    const personalidadValida = validarPersonalidad();
    const descripcionValida = validarDescripcion();
    const tipoValido = validarTipo();
    const estadoValido = validarEstado();
    const fotoValido = validarFoto();

    if (
        nombreValido &&
        edadValida &&
        pesoValido &&
        personalidadValida &&
        descripcionValida &&
        tipoValido &&
        estadoValido
    ) {
        evento.preventDefault();

        alert("Datos válidos. Animal modificado.");
    } else {
        evento.preventDefault();
    }
}


// =========================
// INICIAR VALIDACIONES
// =========================

function iniciarValidacion() {

    formulario.addEventListener("submit", validarFormulario);

    nombre.addEventListener("input", validarNombre);
    edad.addEventListener("input", validarEdad);
    peso.addEventListener("input", validarPeso);
    personalidad.addEventListener("input", validarPersonalidad);
    descripcion.addEventListener("input", validarDescripcion);
    foto.addEventListener("input", validarFoto);

    document.querySelectorAll('input[name="tipo"]').forEach(function (radio) {
        radio.addEventListener("change", validarTipo);
    });

    document.querySelectorAll('input[name="estado"]').forEach(function (radio) {
        radio.addEventListener("change", validarEstado);
    });
}

iniciarValidacion();
