let deP = document.getElementById("deP");
let aP = document.getElementById("aP");
let ingresoP = document.getElementById("ingresoP");
let resultadoP = document.getElementById("resultadoP");
let convertirP = document.getElementById("convertirP");
let deL = document.getElementById("deL");
let aL = document.getElementById("aL");
let ingresoL = document.getElementById("ingresoL");
let resultadoL = document.getElementById("resultadoL");
let convertirL = document.getElementById("convertirL");
let deT = document.getElementById("deT");
let aT = document.getElementById("aT");
let ingresoT = document.getElementById("ingresoT");
let resultadoT = document.getElementById("resultadoT");
let convertirT = document.getElementById("convertirT");
let deTi = document.getElementById("deTi");
let aTi = document.getElementById("aTi");
let ingresoTi = document.getElementById("ingresoTi");
let resultadoTi = document.getElementById("resultadoTi");
let convertirTi = document.getElementById("convertirTi");


function peso(){
    let dePv = deP.value;
    let aPv = aP.value;

    if(ingresoP.value == ""){
        alert("Ingrese un numero valido")
    }

    if(dePv == "kg"){
        if(aPv == "lb"){
            let res = parseFloat(ingresoP.value)*2.205;
            resultadoP.textContent = res;
        }
        else if(aPv == "arroba"){
            let res1 = parseFloat(ingresoP.value)*0.088;
            resultadoP.textContent = res1;
        }
        else if(aPv == "gramos"){
            let res2 = parseFloat(ingresoP.value)*1000;
            resultadoP.textContent = res2;
        }
         else if(aPv == "onzas"){
            let res3 = parseFloat(ingresoP.value)*35.;
            resultadoP.textContent = res3;
        }
        else{
            alert("Error! Vuelve a intentarlo !!!")
        }
    }
    if(dePv == "lb"){
        if(aPv == "kg"){
            let res = parseFloat(ingresoP.value)/2.205;
            resultadoP.textContent = res;
        }
         else if(aPv == "arroba"){
            let res = parseFloat(ingresoP.value)*25;
            resultadoP.textContent = res;
        }
         else if(aPv == "gramos"){
            let res = parseFloat(ingresoP.value)*453.6;
            resultadoP.textContent = res;
        }
         else if(aPv == "onzas"){
            let res = parseFloat(ingresoP.value)*28.35;
            resultadoP.textContent = res;
        }
        else{
            alert("Error! Vuelve a intentarlo !!!")
        }
    }

    if(dePv == "arroba"){
        if(aPv == "kg"){
            let res = parseFloat(ingresoP.value)*12.5;
            resultadoP.textContent = res;
        }
        else if(aPv == "lb"){
            let res = parseFloat(ingresoP.value)*25;
            resultadoP.textContent = res;
        }
        else if(aPv == "gramos"){
            let res = parseFloat(ingresoP.value)*11339.81;
            resultadoP.textContent = res;
        }
        else if(aPv == "onzas"){
            let res = parseFloat(ingresoP.value)*405.72;
            resultadoP.textContent = res;
        }
        else{
            alert("Error! Vuelve a intentarlo !!!")
        }
    }
    if(dePv == "gramos"){
        if(aPv == "kg"){
            let res = parseFloat(ingresoP.value)/1000;
            resultadoP.textContent = res;
        }
        else if(aPv == "lb"){
            let res = parseFloat(ingresoP.value)/453.6;
            resultadoP.textContent = res;
        }
        else if(aPv == "arroba"){
            let res = parseFloat(ingresoP.value)/11339.809;
            resultadoP.textContent = res;
        }
        else if(aPv == "arroba"){
            let res = parseFloat(ingresoP.value)/28.35;
            resultadoP.textContent = res;
        }
        else{
            alert("Error! Vuelve a intentarlo !!!")
        }
    }
    if(dePv == "onzas"){
        if(aPv == "kg"){
            let res = parseFloat(ingresoP.value)/35.274;
            resultadoP.textContent = res;
        }
        else if(aPv == "lb"){
            let res = parseFloat(ingresoP.value)/16;
            resultadoP.textContent = res;
        }
        else if(aPv == "arroba"){
            let res = parseFloat(ingresoP.value)*0.028349523125;
            resultadoP.textContent = res;
        }
        else if(aPv == "gramos"){
            let res = parseFloat(ingresoP.value)*28.35;
            resultadoP.textContent = res;
        }
        else{
            alert("Error! Vuelve a intentarlo !!!")
        }
    }

}

function longitud(){
    let deLv = deL.value;
    let aLv = aL.value;

    if(ingresoL.value == ""){
        alert("Ingrese un numero valido")
    }

    if(deLv == "m"){
        if(aLv == "km"){
            let res = parseFloat(ingresoL.value)/1000;
            resultadoL.textContent = res;
        }
        else if(aLv == "milla"){
            let res1 = parseFloat(ingresoL.value)/1609;
            resultadoL.textContent = res1;
        }
        else if(aLv == "yarda"){
            let res2 = parseFloat(ingresoL.value)*1094;
            resultadoL.textContent = res2;
        }
         else if(aLv == "codo"){
            let res3 = parseFloat(ingresoL.value)*2.25;
            resultadoL.textContent = res3;
        }
        else{
            alert("Error! Vuelve a intentarlo !!!")
        }
    }
    if(deLv == "km"){
        if(aLv == "m"){
            let res = parseFloat(ingresoL.value)*1000;
            resultadoL.textContent = res;
        }
        else if(aLv == "milla"){
            let res = parseFloat(ingresoL.value)/1609;
            resultadoL.textContent = res;
        }
        else if(aLv == "yarda"){
            let res2 = parseFloat(ingresoL.value)/1094;
            resultadoL.textContent = res2;
        }
         else if(aLv == "codo"){
            let res3 = parseFloat(ingresoL.value)/2.25;
            resultadoL.textContent = res3;
        }
        else{
            alert("Error! Vuelve a intentarlo !!!")
        }
    }

    if(deLv == "m"){
        if(aLv == "km"){
            let res = parseFloat(ingresoP.value)/1000;
            resultadoP.textContent = res;
        }
        else if(aPv == "milla"){
            let res1 = parseFloat(ingresoP.value)*0.088;
            resultadoP.textContent = res1;
        }
        else if(aPv == "yarda"){
            let res2 = parseFloat(ingresoP.value)*1000;
            resultadoP.textContent = res2;
        }
         else if(aPv == "codo"){
            let res3 = parseFloat(ingresoP.value)*35.;
            resultadoP.textContent = res3;
        }
        else{
            alert("Error! Vuelve a intentarlo !!!")
        }
    }
    if(deLv == "m"){
        if(aLv == "km"){
            let res = parseFloat(ingresoP.value)/1000;
            resultadoP.textContent = res;
        }
        else if(aPv == "milla"){
            let res1 = parseFloat(ingresoP.value)*0.088;
            resultadoP.textContent = res1;
        }
        else if(aPv == "yarda"){
            let res2 = parseFloat(ingresoP.value)*1000;
            resultadoP.textContent = res2;
        }
         else if(aPv == "codo"){
            let res3 = parseFloat(ingresoP.value)*35.;
            resultadoP.textContent = res3;
        }
        else{
            alert("Error! Vuelve a intentarlo !!!")
        }
    }
    if(dePv == "onzas"){
        if(aPv == "kg"){
            let res = parseFloat(ingresoP.value)/35.274;
            resultadoP.textContent = res;
        }
        else if(aPv == "lb"){
            let res = parseFloat(ingresoP.value)/16;
            resultadoP.textContent = res;
        }
        else if(aPv == "arroba"){
            let res = parseFloat(ingresoP.value)*0.028349523125;
            resultadoP.textContent = res;
        }
        else if(aPv == "gramos"){
            let res = parseFloat(ingresoP.value)*28.35;
            resultadoP.textContent = res;
        }
        else{
            alert("Error! Vuelve a intentarlo !!!")
        }
    }

}



convertirL.addEventListener("click",longitud);
convertirP.addEventListener("click",peso);
