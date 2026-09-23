const mensaje = document.querySelector("#mensaje");
const comprobante = document.querySelector("#comprobante");
const errorMensaje = document.querySelector("#error-mensaje");
const errorComprobante = document.querySelector("#error-comprobante");
const mensajeFormulario = document.querySelector("#mensaje-formulario");

function validarComprobante() {
    let esValido=false

    if(comprobante.files.lentgh > 0) {
        comprobante.classList.remove("invalido");
        errorComprobante.textContent="";
        esValido=true;
    }

    else{
        comprobante.classList.add("invalido");
        errorComprobante.textContent="Adjuntar comprobante.";
    }

    return esValido;
}

function validarMensaje() {
    const mensajeLimpio=mensaje.value.trim();
    let esValido=false;

    if (mensajeLimpio==="" || mensajeLimpio.length>=4) {
        mensaje.classList.remove("invalido");
        errorMensaje.textContent="";
        esValido=true;
    } else {
       mensaje.classList.add("invalido");
       errorMensaje.textContent="Dejar mensaje vacio o escribir al menos 4 caracteres.";
    }

    return esValido;
}

function validarFormulario(evento) {
    const comprobanteValido=validarComprobante();
    const mensajeValido=validarMensaje();

    if (comprobanteValido && mensajeValido) {
        mensajeFormulario.classList.add("valido");
        mensajeFormulario.textContent = "Datos válidos. Donación registrada.";

        evento.preventDefault(); // DESPUES SE SACA, cuando haya servidor
    } else {
        mensajeFormulario.classList.remove("valido");
        mensajeFormulario.textContent = "Revisar los campos marcados antes de continuar.";
        evento.preventDefault();
    }
}

function iniciarValidacion(){
    document.querySelector("#donar").addEventListener("submit", validarFormulario);

    mensaje.addEventListener("input", validarMensaje);
	comprobante.addEventListener("input", validarComprobante);
}
iniciarValidacion();