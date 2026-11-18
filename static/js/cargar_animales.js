const PATRON_EDAD = /^\d{1,2}$/;           // 0 a 99, solo dígitos
const PATRON_PESO = /^\d+(\.\d+)?$/;       // números enteros o con decimales, ej: 8 o 8.5

const nombre = document.querySelector("#nombre");
const errorNombre = document.querySelector("#error-nombre");
const edad = document.querySelector("#edad");
const errorEdad = document.querySelector("#error-edad");
const peso = document.querySelector("#peso");
const errorPeso = document.querySelector("#error-peso");
const personalidad = document.querySelector("#personalidad");
const errorPersonalidad = document.querySelector("#error-personalidad");
const errorCastrado = document.querySelector("#error-castrado");
const foto = document.querySelector("#foto");
const errorFoto = document.querySelector("#error-foto");
const descripcion = document.querySelector("#descripcion");
const errorDescripcion = document.querySelector("#error-descripcion")
const errorTipo = document.querySelector("#error-tipo");
const errorGenero = document.querySelector("#error-genero");

const mensajeFormulario = document.querySelector("#mensaje-formulario");

function validarNombre() {
    const nombreLimpio = nombre.value.trim();
    let esValido = false;

    if (nombreLimpio.length >= 3) {
        nombre.classList.remove("invalido");
        errorNombre.textContent = "";
        esValido = true;
    } else {
        nombre.classList.add("invalido");
        errorNombre.textContent = "Ingresar al menos 3 caracteres.";
    }

    return esValido;
}

// La edad es texto, pero tiene que "parecer" un número (con el patrón dado).
function validarEdad() {
    const edadLimpia = edad.value.trim();
    const edadValida = PATRON_EDAD.test(edadLimpia);
    let esValido = false;

    if (edadValida) {
        edad.classList.remove("invalido");
        errorEdad.textContent = "";
        esValido = true;
    } else {
        edad.classList.add("invalido");
        errorEdad.textContent = "Ingresar una edad válida en años (0-99).";
    }

    return esValido;
}

function validarPeso() {
    const pesoLimpio = peso.value.trim();
    const pesoValido = PATRON_PESO.test(pesoLimpio);
    let esValido = false;

    if (pesoValido) {
        peso.classList.remove("invalido");
        errorPeso.textContent = "";
        esValido = true;
    } else {
        peso.classList.add("invalido");
        errorPeso.textContent = "Ingresar un peso válido, ej: 8 o 8.5.";
    }

    return esValido;
}

function validarPersonalidad() {
    const personalidadLimpia = personalidad.value.trim();
    let esValido = false;

    if (personalidadLimpia.length >= 3) {
        personalidad.classList.remove("invalido");
        errorPersonalidad.textContent = "";
        esValido = true;
    } else {
        personalidad.classList.add("invalido");
        errorPersonalidad.textContent = "Ingresar al menos 3 caracteres.";
    }

    return esValido;
}

function validarDescripcion() {
    const descripcionLimpia = descripcion.value.trim();
    let esValido = false;

    if (descripcionLimpia.length >= 12) {
        descripcion.classList.remove("invalido");
        errorDescripcion.textContent = "";
        esValido = true;
    } else {
        descripcion.classList.add("invalido");
        errorDescripcion.textContent = "Ingresar al menos 12 caracteres.";
    }

    return esValido;
}

function validarGenero() {
    const generoSeleccionado = document.querySelector('input[name="genero"]:checked');
    let esValido = false;

    if (generoSeleccionado !== null) {
        errorGenero.textContent = "";
        esValido = true;
    } else {
        errorGenero.textContent = "Seleccioná un género.";
    }

    return esValido;
}

function validarTipo() {
    const tipoSeleccionado = document.querySelector('input[name="tipo"]:checked');
    let esValido = false;
    if (tipoSeleccionado !== null) {
        errorTipo.textContent = "";
        esValido = true;
    } else {
        errorTipo.textContent = "Seleccioná un tipo.";
    }
    return esValido;
}


// Valida que se haya elegido una opción del grupo (si/no).
function validarCastrado() {
    const castradoSeleccionado = document.querySelector('input[name="castrado"]:checked');
    let esValido = false;

    if (castradoSeleccionado !== null) {
        errorCastrado.textContent = "";
        esValido = true;
    } else {
        errorCastrado.textContent = "Seleccioná una opción.";
    }

    return esValido;
}

// La foto es obligatoria: tiene que haber al menos un archivo adjunto.
function validarFoto() {
    let esValido = false;

    if (foto.files.length > 0) {
        foto.classList.remove("invalido");
        errorFoto.textContent = "";
        esValido = true;
    } else {
        foto.classList.add("invalido");
        errorFoto.textContent = "Tenés que adjuntar una foto.";
    }

    return esValido;
}

function validarFormulario(evento) {
    const nombreValido = validarNombre();
    const edadValida = validarEdad();
    const pesoValido = validarPeso();
    const personalidadValida = validarPersonalidad();
    const descripcionValida = validarDescripcion();
    const tipoValido = validarTipo();
    const castradoValido = validarCastrado();
    const fotoValida = validarFoto();
    const generoValido = validarGenero();

    if (nombreValido &&
        edadValida &&
        pesoValido &&
        personalidadValida &&
        descripcionValida &&
        tipoValido &&
        generoValido &&
        castradoValido &&
        fotoValida) {
        mensajeFormulario.classList.add("valido");
        mensajeFormulario.textContent = "Datos válidos. Animal cargado.";

    } else {
        mensajeFormulario.classList.remove("valido");
        mensajeFormulario.textContent = "Revisar los campos marcados antes de continuar.";
        evento.preventDefault();
    }
}

function iniciarValidacion() {
    document.querySelector("#cargar").addEventListener("submit", validarFormulario);

    nombre.addEventListener("input", validarNombre);
    edad.addEventListener("input", validarEdad);
    peso.addEventListener("input", validarPeso);
    personalidad.addEventListener("input", validarPersonalidad);
    descripcion.addEventListener("input", validarDescripcion);

    foto.addEventListener("input", validarFoto);

    document.querySelectorAll('input[name="tipo"]').forEach(function (radio) {
        radio.addEventListener("change", validarTipo);
    });

    document.querySelectorAll('input[name="castrado"]').forEach(function (radio) {
        radio.addEventListener("change", validarCastrado);
    });

    document.querySelectorAll('input[name="genero"]').forEach(function (radio) {
        radio.addEventListener("change", validarGenero);
    });
}
iniciarValidacion();