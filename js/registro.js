const PATRON_CORREO = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
const PATRON_CONTRASEÑA = /^(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,}$/;
const PATRON_TELEFONO = /^\d{2}-\d{4}-\d{4}$/;
const PATRON_DNI = /^\d{7,8}$/;

const nombre = document.querySelector("#nombre");
const apellido = document.querySelector("#apellido");
const correo = document.querySelector("#correo");
const dni = document.querySelector("#dni");
const fechaNacimiento = document.querySelector("#fecha-nacimiento");
const telefono = document.querySelector("#telefono");
const contraseña = document.querySelector("#contraseña");
const errorNombre = document.querySelector("#error-nombre");
const errorApellido = document.querySelector("#error-apellido");
const errorCorreo = document.querySelector("#error-correo");
const errorFecha = document.querySelector("#error-fecha-nacimiento");
const errorDni = document.querySelector("#error-dni");
const errorTelefono = document.querySelector("#error-telefono");
const errorContraseña= document.querySelector("#error-contraseña");
const mensajeFormulario = document.querySelector("#mensaje-formulario");

// 1. Valida que el nombre tenga al menos tres caracteres.
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
function validarApellido() {
    const apellidoLimpio = apellido.value.trim();
    let esValido = false;

    if (apellidoLimpio.length >= 3) {
        apellido.classList.remove("invalido");
        errorApellido.textContent = "";
        esValido = true;
    } else {
        apellido.classList.add("invalido");
        errorApellido.textContent = "Ingresar al menos 3 caracteres.";
    }

    return esValido;
}
function validarTelefono() {

	const telefonoLimpio = telefono.value.trim();
	const telefonoValido = PATRON_TELEFONO.test(telefonoLimpio);
    let esValido = false;

	if (telefonoValido) {
		telefono.classList.remove("invalido");
		errorTelefono.textContent = "";
		esValido = true;
	} else {
		telefono.classList.add("invalido");
		errorTelefono.textContent = "Formato esperado: 11-1234-5678.";
	}
    return esValido;
}

// 2. El patrón de DNI comprueba entre siete y ocho dígitos.
function validarDni() {

	const dniLimpio = dni.value.trim();
	const dniValido = PATRON_DNI.test(dniLimpio);
    let esValido = false;

	if (dniValido) {
		dni.classList.remove("invalido");
		errorDni.textContent = "";
		esValido = true;
	} else {
		dni.classList.add("invalido");
		errorDni.textContent = "Ingresar un DNI de 7 u 8 dígitos.";
	}
    return esValido;
}
function validarCorreo(){
    let esValido = false;
	const correoLimpio = correo.value.trim();
	const correoValido = PATRON_CORREO.test(correoLimpio);

	if (correoValido) {
		correo.classList.remove("invalido");
		errorCorreo.textContent = "";
        esValido = true;
	} else {
		correo.classList.add("invalido");
		errorCorreo.textContent = "Ingresar un correo valido.";
	}
    return esValido;
}
function validarContraseña(){
    let esValido = false;
	const contraseñaLimpio = contraseña.value;
	const contraseñaValido = PATRON_CONTRASEÑA.test(contraseñaLimpio);

	if (contraseñaValido) {
		contraseña.classList.remove("invalido");
		errorContraseña.textContent = "";
        esValido = true;
	} else {
		contraseña.classList.add("invalido");
		errorContraseña.textContent = "La contraseña debe tener 8 caracteres, una mayúscula, un número y un carácter especial.";
	}
    return esValido;
}
// Valida que la persona tenga al menos 18 años cumplidos.
function validarFecha() {
	const valor = fechaNacimiento.value; // formato "AAAA-MM-DD"
	let edadValida = false;
	let esValido = false;

	if (valor !== "") {
		const [anio, mes, dia] = valor.split("-").map(Number);
		const hoy = new Date();

		let edad = hoy.getFullYear() - anio;
		const todaviaNoCumplio =
			(hoy.getMonth() + 1) < mes ||
			((hoy.getMonth() + 1) === mes && hoy.getDate() < dia);
		if (todaviaNoCumplio) {
			edad--;
		}

		// anio > 1900 evita fechas absurdas mientras se escribe el año
		edadValida = anio > 1900 && edad >= 18;
	}

	if (edadValida) {
		fechaNacimiento.classList.remove("invalido");
		errorFecha.textContent = "";
		esValido = true;
	} else {
		fechaNacimiento.classList.add("invalido");
		errorFecha.textContent = "Tenés que tener al menos 18 años.";
	}

	return esValido;
}

// 4. submit activa la validación; solo se cancela si hay errores o no hay servidor.
function validarFormulario(evento) {
	const contraseñaValida = validarContraseña();
	const correoValido = validarCorreo();
    const nombreValido = validarNombre();
    const fechaValida = validarFecha();
    const apellidoValido = validarApellido();
    const dniValido = validarDni();
    const telefonoValido = validarTelefono();


	if (contraseñaValida && correoValido && nombreValido && fechaValida && apellidoValido && dniValido && telefonoValido) {
		mensajeFormulario.classList.add("valido");
		mensajeFormulario.textContent = "Datos válidos. Cuenta creada.";
        
        evento.preventDefault()//DESPUES SE SACA
	} else {
		// Si hay errores, siempre se cancela el envío para poder corregirlos.
		mensajeFormulario.classList.remove("valido");
		mensajeFormulario.textContent = "Revisar los campos marcados antes de continuar.";
		evento.preventDefault(); // Evita que el formulario se envíe si hay errores.
	}
}

// input vuelve a validar el campo mientras se escribe.
function iniciarValidacion() {
	document.querySelector("#registro").addEventListener("submit", validarFormulario);

	nombre.addEventListener("input", validarNombre);
	apellido.addEventListener("input", validarApellido);
	correo.addEventListener("input", validarCorreo);
	contraseña.addEventListener("input", validarContraseña);
	dni.addEventListener("input", validarDni);
	telefono.addEventListener("input", validarTelefono);
	fechaNacimiento.addEventListener("input", validarFecha);


}
iniciarValidacion();