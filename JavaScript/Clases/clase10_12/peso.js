let deP = document.getElementById("deP");
let aP = document.getElementById("aP");
let ingresoP = document.getElementById("ingresoP");
let resultadoP = document.getElementById("resultadoP");
let select1 = document.getElementById('deP');
let select2 = document.getElementById('aP');

let select = {
    de: '',
    a: ''
}
let selects = JSON.parse(localStorage.getItem('pes'));

if (selects) {
    select = selects;
    select1.value = select.de;
    select2.value = select.a;
}

export function peso(){
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
    select.de = select1.value;
    select.a = select2.value;

    localStorage.setItem('pes', JSON.stringify(select));

}