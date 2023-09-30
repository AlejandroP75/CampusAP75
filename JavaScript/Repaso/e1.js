let entrada = document.getElementById('ingNum');
let boton = document.getElementById('dupli');
let salida = document.getElementById('resu');

function duplicar() {
    let num = parseFloat(entrada.value);
    let doble = num * 2;
    salida.textContent = "Resultado = " + doble;
}

boton.addEventListener("click", duplicar);