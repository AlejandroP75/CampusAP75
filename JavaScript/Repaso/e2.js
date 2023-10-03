let a1 = document.getElementById("a");
let b1 = document.getElementById("b");
let c1 = document.getElementById("c");
let boton = document.getElementById("boton");
let x1res = document.getElementById("x1");
let x2res = document.getElementById("x2");

function calcular(){

    let a = a1.value;
    let b = b1.value;
    let c = c1.value;

    if(a == 0){
        alert("El valor de a no puede ser 0");
    }else if(((b*b) - (4*a*c)) < 0){
        alert("El valor del discriminante es negativo");
    }else{
        let x1 = ((-b+Math.sqrt((b*b)-4*a*c)) / (2*a));
        let x2 = ((-b-Math.sqrt((b*b)-4*a*c)) / (2*a));
        x1res.textContent = "x1 = " + x1;
        x2res.textContent = "x2 = " + x2;
    }
}

boton.addEventListener("click", calcular);

const estiloSelector = document.getElementById('estiloSelector');
const guardarEstilo = document.getElementById('guardarEstilo');
const estilos = document.getElementById('estilos');

guardarEstilo.addEventListener('click', function () {
    const estiloSeleccionado = estiloSelector.value;

    if (estiloSeleccionado) {
        localStorage.setItem('estilo', estiloSeleccionado);
        estilos.setAttribute('href', estiloSeleccionado + '.css');
    }
});

window.addEventListener('load', function () {
    const estiloAlmacenado = localStorage.getItem('estilo');

    if (estiloAlmacenado) {
        estilos.setAttribute('href', estiloAlmacenado + '.css');
        estiloSelector.value = estiloAlmacenado;
    }
});