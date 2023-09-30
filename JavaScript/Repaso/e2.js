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
        x1res.textContent = "X1 = " + x1;
        x2res.textContent = "X2 = " + x2;
    }
}

boton.addEventListener("click", calcular);

