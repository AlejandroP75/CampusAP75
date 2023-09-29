//Generamos el numero aleatorio
function Alea(){
    return Math.round(Math.random() * (11 - 1) + 1);
}
var num1 = document.querySelector(".num1");
var num2 = document.querySelector(".num2");
num1 = Alea();
num2 = Alea();
//Llamamos a los elemntos creados en el html

function generaTion(){

    num1 = Alea();
    num2 = Alea();

    if(num1 > num2){
        console.log("This is a test")

    }
}
//Añadir el evento

const botonAleatorio1 = document.querySelector(".generarAlea1");
botonAleatorio1.addEventListener("click", generaTion);

const botonAleatorio2 = document.querySelector(".generarAlea2");
botonAleatorio2.addEventListener("click", generaTion);