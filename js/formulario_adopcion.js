const familia=document.querySelector("#familia");
const errorfamilia=document.querySelector("#error-familia");
const alergias=document.querySelector("#alergias");
const erroralergias=document.querySelector("#error-alergias");
const mascotas=document.querySelector("#mascotas");
const errormascotas=document.querySelector("#error-mascotas");
const errorTipo=document.querySelector("#error-tipo");
const cuidado=document.querySelector("#cuidado");
const errorcuidado=document.querySelector("#error-cuidado");
const solo=document.querySelector("#tiempo_solo");
const errorsolo=document.querySelector("#error-solo");
const hogar=document.querySelector("#hogar");
const errorhogar=document.querySelector("#error-hogar");

const mensajeFormulario = document.querySelector("#mensaje-formulario");

function validarfamilia() {
    const familiaLimpio = familia.value.trim();
    let esValido = false;

    if (familiaLimpio.length >= 3) {
        familia.classList.remove("invalido");
        errorfamilia.textContent = "";
        esValido = true;
    } else {
        familia.classList.add("invalido");
        errorfamilia.textContent = "Ingresar al menos 3 caracteres.";
    }

    return esValido;
}

function validaralergias() {
    const alergiasLimpio = alergias.value.trim();
    let esValido = false;

    if (alergiasLimpio.length >= 2) {
        alergias.classList.remove("invalido");
        erroralergias.textContent = "";
        esValido = true;
    } else {
        alergias.classList.add("invalido");
        erroralergias.textContent = "Ingresar al menos 2 caracteres.";
    }

    return esValido;
}

function validarmascotas() {
    const mascotasLimpio = mascotas.value.trim();
    let esValido = false;

    if (mascotasLimpio.length >= 2) {
        mascotas.classList.remove("invalido");
        errormascotas.textContent = "";
        esValido = true;
    } else {
        mascotas.classList.add("invalido");
        errormascotas.textContent = "Ingresar al menos 2 caracteres.";
    }

    return esValido;
}

function validarcuidado() {
    const cuidadoLimpio = cuidado.value.trim();
    let esValido = false;

    if (cuidadoLimpio.length >= 3) {
        cuidado.classList.remove("invalido");
        errorcuidado.textContent = "";
        esValido = true;
    } else {
        cuidado.classList.add("invalido");
        errorcuidado.textContent = "Ingresar al menos 3 caracteres.";
    }

    return esValido;
}

function validarsolo() {
    const soloLimpio = solo.value.trim();
    let esValido = false;

    if (soloLimpio.length >= 3) {
        solo.classList.remove("invalido");
        errorsolo.textContent = "";
        esValido = true;
    } else {
        solo.classList.add("invalido");
        errorsolo.textContent = "Ingresar al menos 3 caracteres.";
    }

    return esValido;
}

function validarhogar() {
    const hogarLimpio = hogar.value.trim();
    let esValido = false;

    if (hogarLimpio.length >= 3) {
        hogar.classList.remove("invalido");
        errorhogar.textContent = "";
        esValido = true;
    } else {
        hogar.classList.add("invalido");
        errorhogar.textContent = "Ingresar al menos 3 caracteres.";
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
        errorTipo.textContent = "Seleccioná una opción.";
    }

    return esValido;
}

function validarFormulario(evento) {
    const familiaValido=validarfamilia();
    const alergiasValido=validaralergias();
    const mascotasValido=validarmascotas();
    const cuidadoValido=validarcuidado();
    const soloValido=validarsolo();
    const hogarValido=validarhogar();
    const tipoValido=validarTipo();

    if (familiaValido && alergiasValido && mascotasValido && cuidadoValido && soloValido && hogarValido && tipoValido) {
        mensajeFormulario.classList.add("valido");
        mensajeFormulario.textContent = "Datos válidos. Formulario registrado.";

        evento.preventDefault(); // DESPUES SE SACA, cuando haya servidor
    } else {
        mensajeFormulario.classList.remove("valido");
        mensajeFormulario.textContent = "Revisar los campos marcados antes de continuar.";
        evento.preventDefault();
    }
}

function iniciarValidacion(){
    document.querySelector("#adoptar").addEventListener("submit", validarFormulario);

    familia.addEventListener("input", validarfamilia);
    alergias.addEventListener("input", validaralergias);
    mascotas.addEventListener("input", validarmascotas);
    cuidado.addEventListener("input", validarcuidado);
    solo.addEventListener("input", validarsolo);
    hogar.addEventListener("input", validarhogar);

    document.querySelectorAll('input[name="tipo"]').forEach(function (radio) {
    radio.addEventListener("change", validarTipo);
    });
}
iniciarValidacion();