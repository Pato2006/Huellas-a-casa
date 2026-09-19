const PATRON_CORREO = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
const PATRON_CONTRASEÑA = /^(?=.*[A-Z])(?=.*\d).{8,}$/;


const correo = document.querySelector("#correo");
const contraseña = document.querySelector("#contraseña");
const errorCorreo = document.querySelector("#error-correo");
const errorContraseña= document.querySelector("#error-contraseña");
const mensajeFormulario = document.querySelector("#mensaje-formulario");

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
	const contraseñaLimpio = contraseña.value.trim();
	const contraseñaValido = PATRON_CONTRASEÑA.test(contraseñaLimpio);

	if (contraseñaValido) {
		contraseña.classList.remove("invalido");
		errorContraseña.textContent = "";
        esValido = true;
	} else {
		contraseña.classList.add("invalido");
		errorContraseña.textContent = "La contraseña debe contener 8 caracteres, una letra mayuscula y un número.";
	}
    return esValido;
}

// 4. submit activa la validación; solo se cancela si hay errores o no hay servidor.
function validarFormulario(evento) {
	const contraseñaValida = validarContraseña();
	const correoValido = validarCorreo();

	if (contraseñaValida && correoValido) {
		mensajeFormulario.classList.add("valido");
		mensajeFormulario.textContent = "Datos válidos. Sesión iniciada";
        
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
	//nombre.addEventListener("input", validarNombre);
	correo.addEventListener("input", validarCorreo);
	contraseña.addEventListener("input", validarContraseña);
	document.querySelector("#login").addEventListener("submit", validarFormulario);
}

iniciarValidacion();